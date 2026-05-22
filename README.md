# phishing-email-website

A machine learning-based web application that detects phishing emails using Natural Language Processing (NLP) and classification algorithms.

## 📋 Project Overview

This project implements a phishing email detection system that uses a Naive Bayes classifier trained on email data. Users can paste email content into a web interface, and the application will classify it as either a "PHISHING EMAIL" or a "SAFE EMAIL" based on trained models.

## 📁 Repository Structure

```
phishing-email-website/
├── README.md                          # Project documentation
└── phishing-website/                  # Main application directory
    ├── app.py                         # Flask application and ML model
    ├── emails.csv                     # Training dataset
    └── templates/
        └── index.html                 # Web interface
```

## 📄 File Descriptions

### `phishing-website/app.py`
**Language:** Python  
**Purpose:** Main Flask application and machine learning backend

**Key Features:**
- Loads email training data from `emails.csv`
- Implements text cleaning function to preprocess emails
- Uses TF-IDF (Term Frequency-Inverse Document Frequency) vectorization
- Trains a Multinomial Naive Bayes classifier
- Provides two Flask routes:
  - `/` - Serves the home page (index.html)
  - `/predict` - Handles email prediction requests via POST

**Key Functions:**
- `clean_text(text)` - Converts text to lowercase, removes URLs, and removes special characters

**Dependencies:**
- Flask
- Pandas
- Scikit-learn (TfidfVectorizer, MultinomialNB)
- Joblib

### `phishing-website/emails.csv`
**Language:** CSV  
**Purpose:** Training dataset for the phishing detection model

**Contents:**
- Contains 4 sample emails with labels
- Columns:
  - `text` - Email content
  - `label` - Classification ("safe" or "phishing")

**Sample Data:**
- Phishing examples: "Congratulations! Click here to win money", "Verify your account immediately"
- Safe examples: "Meeting tomorrow at 10 AM", "Project report attached"

### `phishing-website/templates/index.html`
**Language:** HTML/CSS/JavaScript  
**Purpose:** Web user interface for the email detection application

**Features:**
- Responsive design with centered container
- Textarea for users to paste email content
- Submit button to trigger detection
- Loading indicator ("Scanning Email...")
- Result display area showing prediction outcome
- Styled with embedded CSS:
  - Light gray background (#f4f4f4)
  - White content container with shadow
  - Blue submit button with hover effect

**Interaction:**
- Users paste email content in the textarea
- Click "Detect Email" button to submit
- Loading indicator displays while processing
- Result shows "PHISHING EMAIL" or "SAFE EMAIL"

---

## 🚀 To Get Started

### Prerequisites
- Python 3.x
- Flask
- Pandas
- Scikit-learn
- Joblib

### Installation

1. Navigate to the project directory:
   ```bash
   cd phishing-website
   ```

2. Install dependencies:
   ```bash
   pip install flask pandas scikit-learn joblib
   ```

3. Run the Flask application:
   ```bash
   python app.py
   ```

4. Open your browser and navigate to:
   ```
   http://localhost:5000
   ```

## 📊 How It Works

1. **Data Loading** - Emails and labels are loaded from `emails.csv`
2. **Text Preprocessing** - Emails are cleaned by:
   - Converting to lowercase
   - Removing URLs
   - Removing special characters and numbers
3. **Feature Extraction** - TF-IDF vectorization transforms text into numerical features
4. **Model Training** - Multinomial Naive Bayes classifier is trained on the vectorized data
5. **Prediction** - User input is processed through the same pipeline and classified

## 🔧 Technology Stack

- **Backend:** Flask (Python web framework)
- **Machine Learning:** Scikit-learn
- **Data Processing:** Pandas
- **Frontend:** HTML, CSS, JavaScript

## 📝 Note

- The current dataset is minimal (4 samples) for demonstration purposes
- For production use, expand `emails.csv` with a larger, more diverse dataset
- Consider adding cross-validation and model evaluation metrics
- The model is trained every time the application starts; consider pre-training and saving the model

## 🔐 Security Note

This is a demonstration project for educational purposes in understanding phishing detection concepts.

---
**Repository:** [reesdsa13/phishing-email-website](https://github.com/reesdsa13/phishing-email-website)
