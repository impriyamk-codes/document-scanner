import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import streamlit as st
import cv2
import numpy as np
from scanner.scan import scan_document
import img2pdf

# Page config
st.set_page_config(page_title="Document Scanner", layout="wide")

# 🎨 BLUE-GREEN DARK THEME
st.markdown("""
<style>

/* FULL APP BACKGROUND */
html, body, .stApp {
    background-color: #0a192f !important;
    color: #e6f1ff !important;
}

/* Title */
.title {
    font-size: 42px;
    font-weight: 600;
    text-align: center;
    margin-bottom: 5px;
    color: #64ffda;
}

/* Subtitle */
.subtitle {
    text-align: center;
    color: #8892b0;
    margin-bottom: 30px;
}

/* Cards */
.card {
    background: #112240;
    padding: 15px;
    border-radius: 14px;
    border: 1px solid rgba(100,255,218,0.1);
    transition: 0.3s;
}

/* Hover glow */
.card:hover {
    border: 1px solid #64ffda;
    box-shadow: 0 0 20px rgba(100,255,218,0.2);
}

/* File uploader */
section[data-testid="stFileUploader"] {
    border: 1px dashed #64ffda;
    padding: 20px;
    border-radius: 12px;
    background-color: rgba(17,34,64,0.6);
}

/* Download button */
.stDownloadButton>button {
    background: linear-gradient(90deg, #00c6ff, #64ffda);
    color: #0a192f;
    border-radius: 8px;
    border: none;
    padding: 10px 20px;
    font-weight: 600;
}

/* Spinner text */
.stSpinner > div {
    color: #64ffda !important;
}

</style>
""", unsafe_allow_html=True)

# Title
st.markdown('<div class="title">📄 Document Scanner</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Clean. Fast. Reliable.</div>', unsafe_allow_html=True)
st.divider()

# File upload
uploaded_file = st.file_uploader("Upload an image", type=["jpg", "png", "jpeg"])

if uploaded_file is not None:
    file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
    image = cv2.imdecode(file_bytes, 1)

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("### Original")
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.image(image, channels="BGR", use_column_width=True)
        st.markdown('</div>', unsafe_allow_html=True)

    with st.spinner("Processing..."):
        scanned = scan_document(image)

    with col2:
        st.markdown("### Scanned")
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.image(scanned, channels="GRAY", use_column_width=True)
        st.markdown('</div>', unsafe_allow_html=True)

    # Save temp image
    temp_path = "temp.jpg"
    cv2.imwrite(temp_path, scanned)

    # Convert to PDF
    pdf_path = "output.pdf"
    with open(pdf_path, "wb") as f:
        f.write(img2pdf.convert(temp_path))

    st.success("Scan completed!")

    # Download PDF
    with open(pdf_path, "rb") as f:
        st.download_button(
            label="Download PDF",
            data=f,
            file_name="scan.pdf",
            mime="application/pdf"
        )