
import streamlit as st
import requests

st.title("Fake News Detector")
news_input = st.text_area("Type/Paste your news here",height=300)
if st.button("Check News"):
    if not news_input.strip():
        st.error("Please enter some news!")
    else:
        try:
            url = "http://127.0.0.1:8000/predict"
            payload = {"text":news_input}
            response = requests.post(url,json=payload)
            if response.status_code == 200:
                prediction = response.json().get("Prediction")
                if prediction == "Real":
                    st.success("This news is likely REAL.")
                elif prediction == "Fake":
                    st.error("This news is likely FAKE.")
                else:
                    st.info(f"Prediction: {prediction}")
            else:
                st.error(f"API Error: {response.status_code} - {response.text}")
        except Exception as e:
            st.error(f"Error calling API: {e}")