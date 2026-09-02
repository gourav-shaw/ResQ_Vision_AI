import streamlit as st
from ultralytics import YOLO
from PIL import Image

st.set_page_config(page_title="C2A Human Detection", layout="centered")

@st.cache_resource
def load_model():
    return YOLO('best.pt')

model = load_model()

st.title("C2A Human Detection — Disaster Scenario Prototype")
st.write("YOLO11n model trained on the C2A dataset for human detection in disaster imagery.")

conf = st.slider("Confidence threshold", 0.05, 0.9, 0.25, 0.05)

uploaded_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    img = Image.open(uploaded_file).convert("RGB")
    st.image(img, caption="Uploaded image", use_container_width=True)

    with st.spinner("Running detection..."):
        results = model(img, conf=conf)
        plotted = results[0].plot()[..., ::-1]  # BGR -> RGB

    st.image(plotted, caption=f"Detections ({len(results[0].boxes)} found)", use_container_width=True)
