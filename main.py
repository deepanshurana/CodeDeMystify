import os
import streamlit as st
from text_to_speech import text_to_speech
from invoke_ai import retrieve_code_explanation, retrieve_code_language
import constants


def header_display():
    st.header("Welcome to Code Explainer")
    st.title("Upload your code here.")


def display_widgets():
    file = st.file_uploader("Upload script.")
    text = st.text_area("Copy and paste your code here. ")

    if not (text or file):
        st.error("Take one option above")

    return file, text


def retrieve_content(file):
    return file.getvalue().decode("utf-8")


def extract_code():
    uploaded_text, pasted_code = display_widgets()

    if uploaded_text:
        return retrieve_content(uploaded_text)
    return pasted_code or ""


def delete_file_if_exists(file_paths):
    try:
        for file_path in file_paths:
            if os.path.exists(file_path):
                os.remove(file_path)
    except Exception as e:
        return


def main_method():
    delete_file_if_exists(["language.mp3", "explanation.mp3"])
    header_display()
    if code_to_explain := extract_code():
        with st.spinner(text=constants.THOUGHT_PROCESS):
            lang, explanation = retrieve_code_language(
                code=code_to_explain
            ), retrieve_code_explanation(code=code_to_explain)

        with st.spinner(text=constants.INTENSE_THOUGH_PROCESS):
            text_to_speech(lang, "language")

        with st.spinner(text=constants.LANGUAGE_FOUND):
            text_to_speech(explanation, "explanation")

        st.success(constants.EXPLANATION_DONE)
        st.warning(constants.TURN_ON_VOLUME)

        st.markdown(f"**language:** {lang}")
        st.audio("language.mp3")

        st.markdown(f"**Explanation:** {explanation}")
        st.audio("explanation.mp3")


if __name__ == "__main__":
    main_method()
