import streamlit as st
import pandas as pd

df = pd.read_excel("budget.xlsx")

st.title("Budget Dashboard")

st.dataframe(df)
