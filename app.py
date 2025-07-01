import streamlit as st
import pandas as pd
import pickle

# Load model, encoder, and columns
with open("model.pkl", "rb") as f:
    model = pickle.load(f)

with open("label_encoder.pkl", "rb") as f:
    le = pickle.load(f)

with open("feature_columns.pkl", "rb") as f:
    feature_columns = pickle.load(f)

st.title("🧴 Sunscreen Recommender System")

# Inputs
skin_tone = st.selectbox("Skin Tone", ["fair", "medium", "dark"])
uv_index = st.slider("UV Index", 0, 11)
cloud_coverage = st.slider("Cloud Coverage (%)", 0, 100)
location_type = st.selectbox("Location", ["beach", "city", "mountain"])
time_of_day = st.selectbox("Time of Day", ["morning", "afternoon", "evening"])
activity_level = st.selectbox("Activity", ["indoor", "light_outdoor", "heavy_outdoor"])

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

# Predict
if st.button("Recommend SPF"):
    prediction = model.predict(df)[0]
    label = le.inverse_transform([prediction])[0]
    st.success(f"✅ Recommended SPF: **{label}**")
