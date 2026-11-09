import streamlit as st

st.set_page_config(
    page_title="ASL Alphabet Recognition",
    page_icon="🤟",
    layout="wide"
)

st.title("🤟 ASL Alphabet Recognition")

st.write(
    "Welcome to the American Sign Language "
    "Alphabet Recognition System."
)

st.subheader("Project Features")

st.write("""
- Hand gesture recognition
- ASL alphabet detection
- Image-based hand recognition
- Real-time recognition (if supported)
""")

st.info("Your Streamlit application is running!")
