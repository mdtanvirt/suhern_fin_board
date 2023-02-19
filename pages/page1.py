import streamlit as st
from streamlit_option_menu import option_menu

st.title("Page - 1")


# 1. as Side menu
with st.sidebar:
    selected = option_menu(
        menu_title="Main Menu",
        options=["Home", "Project", "Page"],
        icons=["house", "book", "envelope"],
        default_index=0,
        orientation="horizontal",
    )


if selected == "Home":
    st.title(f"You select {selected}")

if selected == "Project":
    st.title(f"You select {selected}")

if selected == "Page":
    st.title(f"You select {selected}")

