## 🩺 Interactive Breast Cancer Diagnostic Assistant

An interactive machine learning dashboard that translates complex, multidimensional clinical tumor metrics into real-time diagnostic insights. 

## 🔍 Project Overview
In clinical oncology, evaluating tumor characteristics manually requires cross-referencing multiple structural data points, which can be time-consuming. This project bridges the gap between raw data and medical usability by providing a web-based clinical assistant. The system takes quantitative cellular metrics and processes them through an optimized machine learning pipeline to compute classification probabilities instantaneously.**Crucially, this system is designed to serve as a supportive tool rather than an automated decision-maker, emphasizing that while AI can rapidly detect and flag anomalies, the final diagnostic validation remains strictly in the hands of the medical professional.**

## 🎯 Objective
The primary objective of this project is to develop and deploy a highly sensitive predictive tool capable of distinguishing between benign and malignant breast tissue. By focusing heavily on maximizing model sensitivity (recall) for malignant cases, the project aims to minimize false-negative rates—ensuring critical cases are never missed.
**The core goal is to provide reliable data insights that aid human evaluation, reinforcing that the technology acts as a diagnostic companion while final clinical decisions rest entirely on human judgment.**

## 💻 Technology Used
- **Programming Language:** Python 3
- **Data Engineering & Analysis:** Pandas, NumPy
- **Machine Learning Infrastructure:** Scikit-Learn (SciPy stack)
- **Model Serialization:** Pickle
- **Data Visualization:** Matplotlib
- **Web UI & Cloud Deployment:** Streamlit Framework

## 📊 Dataset Information
The underlying diagnostic model was built using a clinical dataset containing records for **569 patients**:
- **Attributes Analyzed:** 30 distinct feature measurements derived from digitized images of fine needle aspirates (FNA) of breast masses.
- **Key Metrics Included:** Mean Radius, Mean Texture, Mean Perimeter, Mean Area, Mean Smoothness, Mean Compactness, Mean Concavity, and Mean Concave Points.
- **Target Label Mapping:** Categorical text outcomes were transformed into clean binary targets:
  - `0` ➡️ **Malignant**
  - `1` ➡️ **Benign**

## 🤖 Machine Learning Model
A **Logistic Regression** classifier was curated and trained for this application. Logistic Regression was selected over black-box models because it natively outputs clear prediction probabilities (confidence intervals) rather than rigid classifications. This allows users to see the *exact probability gradient* of a diagnosis, matching clinical needs where uncertainty levels are just as important as the final classification.

## 📈 Model Performance
The model was validated using a strict, un-shuffled **80/20 train-test split**, evaluating its final generalizing capability against **114 unseen test samples**:

- **Overall Test Accuracy:** `96%`
- **Malignant Sensitivity (Class 0):** Correctly detected `70 out of 71` total malignant cases (**99% Recall**).
- **Benign Sensitivity (Class 1):** Correctly detected `39 out of 43` total benign cases.

### Classification Report Summary:

| Diagnostic Class | Precision | Recall (Sensitivity) | F1-Score | Support |

| **0 (Malignant)** | `0.95` | `0.99` | `0.97` | 71 |

| **1 (Benign)** | `0.97` | `0.91` | `0.94` | 43 |

---

## 🚀 App Features
- **Interactive Control Sliders:** Side-panel controls let users systematically alter specific cellular dimensions (e.g., mean radius, mean texture, compactness) to test mathematical edge-cases.
- **Real-Time Inference Engine:** Instantly executes backend mathematical model equations using pre-serialized weights via `pickle` the exact moment a slider is adjusted.
- **Dynamic Graphical Probabilities:** Renders a clean, automated visual horizontal bar chart demonstrating the exact model confidence breakdown between Benign and Malignant thresholds.

## Application Screenshot

<a href="https://breast-cancer-app-e7nsbt7xwg3swzu8fzugip.streamlit.app/" target="_blank">
<img width="1600" height="782" alt="image" src="https://github.com/user-attachments/assets/8982202c-0cce-4242-af0a-5e52f6f9e19a" />
</a>

## Result

<a href="https://breast-cancer-app-e7nsbt7xwg3swzu8fzugip.streamlit.app/" target="_blank">
<img width="1600" height="782" alt="image" src="https://github.com/user-attachments/assets/39d8ce33-952b-463c-a3d0-0e6b9636f651" />

</a>
