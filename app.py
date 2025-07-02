%%writefile app.py
# app.py
import streamlit as st
import pandas as pd
import pickle

st.set_page_config(page_title="Sunscreen Recommender", page_icon="🧴", layout="centered")

st.markdown("<h1 style='text-align: center; color: #ff914d;'>🧴 Sunscreen Recommender System</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; font-size: 18px;'>Get the best SPF suggestion based on your environment and activity!</p>", unsafe_allow_html=True)
st.markdown("---")

# Load model and artifacts
try:
    with open("model.pkl", "rb") as f:
        model = pickle.load(f)

    with open("label_encoder.pkl", "rb") as f:
        le = pickle.load(f)

    with open("feature_columns.pkl", "rb") as f:
        feature_columns = pickle.load(f)
except Exception as e:
    st.error(f"⚠️ Error loading model files: {e}")
    st.stop()

# Input layout
col1, col2 = st.columns(2)

with col1:
    skin_tone = st.selectbox("🎨 Skin Tone", ["fair", "medium", "dark"])
    uv_index = st.slider("🌞 UV Index", 0, 11, 5)
    location_type = st.selectbox("📍 Location", ["beach", "city", "mountain"])

with col2:
    cloud_coverage = st.slider("☁️ Cloud Coverage (%)", 0, 100, 50)
    time_of_day = st.selectbox("🕒 Time of Day", ["morning", "afternoon", "evening"])
    activity_level = st.selectbox("🏃 Activity", ["indoor", "light_outdoor", "heavy_outdoor"])

# Prepare input
input_dict = {
    "uv_index": uv_index,
    "cloud_coverage": cloud_coverage,
    f"skin_tone_{skin_tone}": 1,
    f"location_type_{location_type}": 1,
    f"time_of_day_{time_of_day}": 1,
    f"activity_level_{activity_level}": 1
}

df = pd.DataFrame([input_dict])
for col in feature_columns:
    if col not in df.columns:
        df[col] = 0
df = df[feature_columns]

# Prediction button
st.markdown("---")
if st.button("🚀 Recommend SPF"):
    with st.spinner("Analyzing your conditions..."):
        try:
            prediction = model.predict(df)[0]
            label = le.inverse_transform([prediction])[0]
            st.markdown(
                f"<div style='text-align:center; font-size: 24px; color: green;'>✅ Recommended SPF: <strong>{label}</strong></div>",
                unsafe_allow_html=True
            )
        except Exception as e:
            st.error(f"Prediction error: {e}")
