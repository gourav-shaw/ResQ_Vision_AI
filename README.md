# ResQVision AI

**Human detection in disaster scenarios using YOLO11**

ResQVision AI is a prototype object detection system built to identify humans in disaster-affected environments — collapsed buildings, floods, fires, and traffic incidents — to support future search-and-rescue applications.

🔗 **Live demo:** [resqvisionai.streamlit.app](https://resqvisionai.streamlit.app/)

---

## Overview

The model is trained on the **C2A dataset**, which combines real aerial disaster background imagery with composited human figures, giving the model exposure to human presence across a wide range of disaster scenarios without relying on scarce, ethically sensitive real casualty photos.

A trained [YOLO11x](https://github.com/ultralytics/ultralytics) model is deployed as an interactive web app using **Streamlit**, allowing anyone to upload an image and get real-time human detection results with an adjustable confidence threshold.

---

## Features

- Upload any image and detect humans in disaster-like scenes
- Adjustable confidence threshold slider to control detection sensitivity
- YOLO11x model for high-accuracy detection
- Fully deployed, publicly accessible web app (no installation needed)

---

## Model Details

| Metric | Value |
|---|---|
| Architecture | YOLO11x |
| Classes | 1 (`human`) |
| Training data | C2A dataset |
| Image size | 640x640 |
| Epochs | 100 |
| Precision | 0.89 |
| Recall | 0.82 |
| mAP50 | 0.82 |
| mAP50-95 | 0.61 |

> Evaluated on the held-out C2A test split. Strong precision and recall indicate reliable human detection performance in disaster-scenario imagery, though real-world (non-synthetic) generalization may vary — see Future Improvements.

---

## Tech Stack

- **Model:** Ultralytics YOLO11
- **Training:** Google Colab (GPU)
- **Deployment:** Streamlit Community Cloud
- **Dataset:** [C2A Dataset](https://www.kaggle.com/datasets/rgbnihal/c2a-dataset)

---

## Running Locally

```bash
git clone https://github.com/yourusername/resq_vision_ai.git
cd resq_vision_ai
pip install -r requirements.txt
streamlit run app.py
```

Make sure `best.pt` (trained model weights) is present in the project root before running.

---

## Project Structure

```
resq_vision_ai/
├── app.py              # Streamlit application
├── best.pt             # Trained YOLO11x weights
├── requirements.txt    # Python dependencies
├── packages.txt         # System-level dependencies (for OpenCV)
└── README.md
```

---

## Future Improvements

- Fine-tune on real disaster imagery (e.g. AIDER dataset) to close the synthetic-to-real domain gap
- Optimize for edge deployment (ONNX/TensorRT) for use directly on drone hardware
- Expand dataset coverage to night imagery, occluded scenes, and varied camera angles

---

## Acknowledgements

- [C2A Dataset](https://www.kaggle.com/datasets/rgbnihal/c2a-dataset) by rgbnihal
- [AIDER Dataset](https://zenodo.org/records/3888300) by Christos Kyrkou, KIOS COE, University of Cyprus
- [Ultralytics YOLO11](https://github.com/ultralytics/ultralytics)
