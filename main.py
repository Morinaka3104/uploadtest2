import streamlit as st

with open("1-1.pdf", "rb") as pdf_file:
    PDFbyte = pdf_file.read()

st.download_button(label="Download PDF Tutorial",
        data=PDFbyte,
        file_name="1-1.pdf",
        mime='application/octet-stream')