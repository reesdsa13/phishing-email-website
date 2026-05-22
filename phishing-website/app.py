from flask import Flask, render_template, request
import pandas as pd
import re
import joblib

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB

app = Flask(__name__)

# Dataset
data = pd.read_csv("emails.csv")

# Convert labels
data['label_num'] = data.label.map({
    'safe':0,
    'phishing':1
})

# Clean text
def clean_text(text):

    text = text.lower()

    text = re.sub(r'http\\S+', '', text)

    text = re.sub(r'[^a-zA-Z]', ' ', text)

    return text

# Apply cleaning
data['cleaned'] = data['text'].apply(clean_text)

# Features
X = data['cleaned']

y = data['label_num']

# Vectorization
vectorizer = TfidfVectorizer(stop_words='english')

X_vectorized = vectorizer.fit_transform(X)

# Train model
model = MultinomialNB()

model.fit(X_vectorized, y)

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/predict', methods=['POST'])
def predict():

    email = request.form['email']

    cleaned_email = clean_text(email)

    vector = vectorizer.transform([cleaned_email])

    prediction = model.predict(vector)

    if prediction[0] == 1:
        result = "PHISHING EMAIL"
    else:
        result = "SAFE EMAIL"

    return render_template(
        "index.html",
        prediction_text=result
    )

if __name__ == "__main__":
    app.run(debug=True)