import streamlit as st
import pandas as pd
import pickle
import numpy as np

# Load model
with open('material_model.pkl', 'rb') as f:
    model, scaler, df = pickle.load(f)

st.set_page_config(page_title="Material Selector AI", layout="wide")
st.title("⚙️ Mechanical Material Selection AI")

# Sidebar for inputs
st.sidebar.header("Design Requirements")
su = st.sidebar.number_input("Ultimate Strength (MPa)", value=500)
sy = st.sidebar.number_input("Yield Strength (MPa)", value=350)
e = st.sidebar.number_input("Young's Modulus (MPa)", value=200000)
ro = st.sidebar.number_input("Target Density (kg/m3)", value=7800)

if st.sidebar.button("Find Materials"):
    user_input = scaler.transform([[su, sy, e, ro]])
    dist, ind = model.kneighbors(user_input)
    
    st.subheader("Top 5 Recommended Materials")
    st.dataframe(df.iloc[ind[0]][['Material', 'Su', 'Sy', 'E', 'Ro']])