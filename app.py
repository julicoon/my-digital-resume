from pathlib import Path

import streamlit as st
from PIL import Image

# --- PATH SETTINGS ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "assets" / "Motivational_Letter.pdf"
profile_pic = current_dir / "assets" / "Foto-bewerbung.png"
cv_file = current_dir / "assets" / "CV.pdf"
records_file = current_dir / "assets" / "records.pdf"

# --- GENERAL SETTINGS ---
PAGE_TITLE = "Digital Resume | Julia Peham"
PAGE_ICON = "👩‍🔬"
NAME = "Julia Peham, BSc"
DESCRIPTION = """
Behaviour, Neurobiology and Cognition master's student at the University of Vienna, assisting as a tutor and intern."""
EMAIL = "julia.peham@univie.ac.at"

st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)

# --- LOAD CSS, PDF & PROFILE PIC ---
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
with open(cv_file, "rb") as pdf_file:
    CVbyte = pdf_file.read()
with open(records_file, "rb") as pdf_file:
    RECORDSbyte = pdf_file.read()
profile_pic = Image.open(profile_pic)


# --- HERO SECTION ---
col1, col2 = st.columns(2, gap="small")
with col1:
    st.image(profile_pic, width=300)
    
with col2:
    st.title(NAME)
    st.write(DESCRIPTION)
    st.download_button(
        label=" 📄 Download Motivational Letter",
        data=PDFbyte,
        file_name=resume_file.name,
        mime="application/octet-stream"

    )
    st.download_button(
        label=" 📄 Download CV",
        data=CVbyte,
        file_name=cv_file.name,
        mime="application/octet-stream"

    )

    st.download_button(
        label=" 📄 Transcript of Records",
        data=RECORDSbyte,
        file_name=records_file.name,
        mime="application/octet-stream"

    )
    st.write("📧", EMAIL)


# --- EXPERIENCE & QUALIFICATIONS --- #
st.write("#")
st.subheader("Why I'm Passionate about This Opportunity")
st.write("#")
st.write(
    """
    - ✔  Driven to continuously expand my knowledge and skills through learning opportunities
    
    - ✔  Dedicated to advancing scientific research through the application of new technologies
    - ✔  Passionate about exploring the intricacies of animal communication and wildlife biology
    - ✔  Excited to contribute to the scientific community through the publication of research findings
    """
)












