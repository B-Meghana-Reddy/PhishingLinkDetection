import streamlit as st
import pickle
import re
import socket
import whois
import requests
from urllib.parse import urlparse
from bs4 import BeautifulSoup
import datetime
import pandas as pd

# Load trained model
model = pickle.load(open("Stacking.pkl", "rb"))  # change path if needed

# Extract features from URL
def featureExtraction(url):
    features = {}

    # Have_IP
    features['Have_IP'] = 1 if re.match(r"^(http|https)://\d+\.\d+\.\d+\.\d+", url) else 0

    # Have_At
    features['Have_At'] = 1 if '@' in url else 0

    # URL_Length
    features['URL_Length'] = len(url)

    # URL_Depth
    features['URL_Depth'] = len(urlparse(url).path.strip('/').split('/'))

    # Redirection '//'
    features['Redirection'] = 1 if '//' in urlparse(url).path else 0

    # https in domain part
    domain = urlparse(url).netloc
    features['https_Domain'] = 1 if 'https' in domain else 0

    # TinyURL
    features['TinyURL'] = 1 if len(url) < 20 else 0

    # Prefix/Suffix
    features['Prefix/Suffix'] = 1 if '-' in domain else 0

    # DNS_Record
    try:
        socket.gethostbyname(domain)
        features['DNS_Record'] = 1
    except:
        features['DNS_Record'] = 0

    # Web Traffic (Alexa rank or similar proxy)
    try:
        response = requests.get(url, timeout=5)
        features['Web_Traffic'] = 1 if response.status_code == 200 else 0
    except:
        features['Web_Traffic'] = 0

    # Domain Age and Domain End
    try:
        domain_info = whois.whois(domain)
        creation_date = domain_info.creation_date
        expiration_date = domain_info.expiration_date

        if isinstance(creation_date, list):
            creation_date = creation_date[0]
        if isinstance(expiration_date, list):
            expiration_date = expiration_date[0]

        current_date = datetime.datetime.now()

        features['Domain_Age'] = 1 if (current_date - creation_date).days > 180 else 0
        features['Domain_End'] = 1 if (expiration_date - current_date).days > 180 else 0
    except:
        features['Domain_Age'] = 0
        features['Domain_End'] = 0

    # iFrame
    try:
        soup = BeautifulSoup(requests.get(url, timeout=5).text, 'html.parser')
        features['iFrame'] = 1 if soup.find_all('iframe') else 0
    except:
        features['iFrame'] = 0

    # Mouse_Over
    try:
        features['Mouse_Over'] = 1 if re.search(r"onmouseover\s*=\s*['\"]?window\.status", soup.text) else 0
    except:
        features['Mouse_Over'] = 0

    # Right_Click
    try:
        features['Right_Click'] = 1 if re.search(r"event.button ?== ?2", soup.text) else 0
    except:
        features['Right_Click'] = 0

    # Web_Forwards (simplified: too many redirects)
    try:
        response = requests.get(url, timeout=5, allow_redirects=True)
        features['Web_Forwards'] = 1 if len(response.history) > 2 else 0
    except:
        features['Web_Forwards'] = 0

    return list(features.values()), features

# ----------- Streamlit UI -----------
st.set_page_config(page_title="Phishing URL Detector", layout="centered")
st.title("🔍 Phishing Website Detection App")
st.markdown("Enter a website URL to check if it is **phishing** or **legitimate**.")

url_input = st.text_input("🌐 Enter the URL:")

if st.button("Predict"):
    if url_input:
        st.write("Extracting features...")

        features_list, features_dict = featureExtraction(url_input)

        try:
            prediction = model.predict([features_list])[0]
            result = "🚨 Phishing" if prediction == 1 else "✅ Legitimate"

            st.subheader("🔎 Prediction Result")
            st.success(f"**Final Verdict:** {result}")

            # st.markdown("### 🧬 Feature Breakdown")
            for name, val in features_dict.items():
                print(f"**{name}**: `{val}`")

        except Exception as e:
            st.error(f"Prediction failed: {e}")
    else:
        st.warning("Please enter a valid URL.")
