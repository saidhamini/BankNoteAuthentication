import streamlit as st
import requests

# FastAPI endpoint
FASTAPI_URL = "http://127.0.0.1:8000/predict"

st.title("📝 Bank Note Authentication")
st.markdown("Enter the banknote features to predict if it is **Authentic or Fake**.")

# Input fields
variance = st.number_input("Variance", value=0.0, format="%.4f")
skewness = st.number_input("Skewness", value=0.0, format="%.4f")
curtosis = st.number_input("Curtosis", value=0.0, format="%.4f")
entropy = st.number_input("Entropy", value=0.0, format="%.4f")

# Submit button
if st.button("🔍 Predict"):
    input_data = {
        "variance": variance,
        "skewness": skewness,
        "curtosis": curtosis,
        "entropy": entropy
    }
    
    try:
        response = requests.post(FASTAPI_URL, json=input_data)
        result = response.json()["prediction"]
        st.success(f"**Prediction:** {result}")
    except Exception as e:
        st.error("Error connecting to API. Make sure FastAPI is running.")
