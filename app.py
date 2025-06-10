import streamlit as st
from analysis_and_model import analysis_and_model_page
from presentation import presentation_page

pages = {
    "🧪Анализ и модель": analysis_and_model_page,
    "🎞Презентация": presentation_page
}

selected_page = st.sidebar.selectbox("Страницы", list(pages.keys()))
pages[selected_page]()