import streamlit as st

st.title("Color picker app")

color = st.color_picker("Pick a Color","#00f900")

st.write("You selected",color)