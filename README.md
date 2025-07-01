https://sunscreenrecommender-lrqlvrwtm88hpms2easx6t.streamlit.app/
# Sunscreen_Recommender
 Sunscreen Recommender System using Machine Learning A smart web app that suggests the best sunscreen SPF level for you based on your skin tone, location, time of day, UV index, and activity level. Built using Python, trained in Google Colab, and deployed with Streamlit Cloud.
# 🧴 Sunscreen Recommender System

This is a smart machine learning-based web app that recommends the most suitable sunscreen SPF (15 / 30 / 50+) based on your personal and environmental conditions like:

- 👤 Skin Tone (fair, medium, dark)
- 🌞 UV Index
- ☁️ Cloud Coverage
- 📍 Location Type (beach, city, mountain)
- 🕒 Time of Day (morning, afternoon, evening)
- 🏃 Activity Level (indoor, light outdoor, heavy outdoor)

## 📌 How It Works

The model was trained using a Random Forest Classifier in Google Colab and deployed using **Streamlit Cloud**.

### Input
User selects values for 6 features using dropdowns/sliders.

### Output
The app displays a **recommended SPF**:
- SPF 15
- SPF 30
- SPF 50+

## 🧠 ML Model

- Model: `RandomForestClassifier`
- Preprocessing: One-hot encoding for categorical features
- Label Encoding for target SPF labels
- Saved using `pickle` and reloaded during prediction

## 🚀 How to Run It Locally

```bash
# Clone the repo
git clone https://github.com/yourusername/sunscreen-app.git
cd sunscreen-app

# Install dependencies
pip install -r requirements.txt

# Run the app
streamlit run app.py
