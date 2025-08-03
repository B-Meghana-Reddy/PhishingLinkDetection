# 🔐 Phishing Website Detection using Machine Learning

This project is a web-based tool that detects **phishing websites** using machine learning models. Users can input any URL, and the system will classify it as **phishing** or **legitimate** based on trained classifiers and URL feature extraction.

## 🚀 Live App

🔗 [Click here to try the live app](https://phishinglink-detect.streamlit.app) — powered by Streamlit.

---

## 📊 Model Performance Summary

The following models were trained and evaluated. The **Stacking classifier** showed the best performance based on test accuracy.

| Model         | Train Accuracy | Test Accuracy |
|---------------|----------------|---------------|
| Decision Tree | 0.816          | 0.804         |
| Random Forest | 0.822          | 0.812         |
| MLP           | 0.862          | 0.849         |
| XGBoost       | 0.870          | 0.853         |
| AutoEncoder   | 0.521          | 0.525         |
| SVM           | 0.803          | 0.797         |
| CatBoost      | 0.870          | 0.853         |
| **Stacking**  | **0.870**      | **0.852**     |

---

## 🧠 Overview

Phishing websites mimic legitimate websites to trick users into sharing sensitive data. This project uses **URL-based feature extraction** and **machine learning** to detect such threats.

---

## ✅ Features

- ✔️ Real-time URL evaluation
- ✔️ Feature-based detection (no page scraping)
- ✔️ Supports `.pkl` based pre-trained model
- ✔️ Clean UI with Streamlit
- ✔️ Final model: **Stacking Classifier** for optimal accuracy

---

## 📂 Dataset Sources

- `1.Benign_list_big_final.csv` – Legitimate URLs
- `2.online-valid.csv` – Verified phishing URLs
- `5.urldata.csv` – Combined dataset after cleaning and preprocessing

---

## Intall Dependencies
pip install -r requirements.txt

---
## Tech Stack

| Component                        | Use                      |
| -------------------------------- | ------------------------ |
| Python                           | Programming Language     |
| Scikit-learn                     | ML Pipelines             |
| XGBoost / CatBoost               | Advanced Ensemble Models |
| Streamlit                        | Web App UI               |
| TensorFlow + Keras               | AutoEncoder              |
| Pickle                           | Model Serialization      |
| Pandas / NumPy                   | Data Preprocessing       |
| BeautifulSoup / Requests / Whois | URL Metadata Analysis    |

---

Dataset credit: shreyagopal/Phishing-Website-Detection
