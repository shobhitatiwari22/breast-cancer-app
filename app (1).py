import streamlit as st
import numpy as np
import pickle
import matplotlib.pyplot as plt

# 1. List of 30 feature names matching your dataset
features = [
    'mean radius', 'mean texture', 'mean perimeter', 'mean area', 'mean smoothness',
    'mean compactness', 'mean concavity', 'mean concave points', 'mean symmetry', 'mean fractal dimension',
    'radius error', 'texture error', 'perimeter error', 'area error', 'smoothness error',
    'compactness error', 'concavity error', 'concave points error', 'symmetry error', 'fractal dimension error',
    'worst radius', 'worst texture', 'worst perimeter', 'worst area', 'worst smoothness',
    'worst compactness', 'worst concavity', 'worst concave points', 'worst symmetry', 'worst fractal dimension'
]

# Set up page configurations
st.set_page_config(layout="wide", page_title="Breast Cancer Diagnostics")
st.title("🩺 Breast Cancer Diagnostic Assistant")
st.write("Adjust patient clinical parameters on the left panel to run diagnostic analysis.")

# 2. Build the sidebar layout for 30 feature sliders
st.sidebar.header("Patient Tumor Metrics")
input_values = []

for feature in features:
    val = st.sidebar.slider(
        label=feature.title(),
        min_value=0.0,
        max_value=250.0, # Adjust standard boundaries as needed
        value=10.0,      # Default starting point
        step=0.1
    )
    input_values.append(val)

# Convert inputs into the 2D matrix layout scikit-learn expects
input_array = np.array([input_values])

# 3. Main Action Trigger Button
if st.button("Run Diagnostic Analysis", type="primary"):
    # Load the saved model weights
    with open('breast_cancer_model.pkl', 'rb') as f:
        model = pickle.load(f)

    prediction = model.predict(input_array)
    probabilities = model.predict_proba(input_array)[0] # Grab probabilities array

    classes = ['Malignant', 'Benign']
    result = classes[prediction[0]]

    # Render clear status boxes
    st.subheader("Analysis Verdict")
    if result == 'Malignant':
        st.error(f"The model predicts: *{result.upper()}*")
    else:
        st.success(f"The model predicts: *{result.upper()}*")

    # 4. Generate clean probability visualization chart
    fig, ax = plt.subplots(figsize=(7, 2.5))
    ax.barh(classes, probabilities, color=['#ff4d4d', '#4da6ff'])
    ax.set_xlim(0, 1)
    ax.set_xlabel('Model Confidence (Probability)')

    # Overlay statistical percentages onto the chart graphics
    for index, value in enumerate(probabilities):
        text_x = value - 0.12 if value > 0.15 else value + 0.02
        text_color = 'white' if value > 0.15 else 'black'
        ax.text(text_x, index, f"{value*100:.1f}%", va='center', color=text_color, fontweight='bold')

    plt.tight_layout()
    st.pyplot(fig)
