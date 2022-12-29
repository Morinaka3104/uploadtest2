import streamlit as st

with open("第2章 解約および解約返戻金.pdf", "rb") as pdf_file:
    PDFbyte = pdf_file.read()

st.download_button(label="Download PDF Tutorial",
        data=PDFbyte,
        file_name="第2章 解約および解約返戻金.pdf",
        mime='application/octet-stream')
