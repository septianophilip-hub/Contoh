import streamlit as st

st.title("Budget Dashboard")

budget = 100000000
actual = 65000000

st.metric(
    "Remaining Budget",
    f"Rp {budget-actual:,.0f}"
)

st.progress(actual/budget)
