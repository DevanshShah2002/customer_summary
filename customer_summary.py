import streamlit as st
import pandas as pd

# ---------- Page Config ----------
st.set_page_config(page_title="Customer Summary", layout="centered")

# ---------- Sample Data ----------
data = pd.read_csv("customer_summary.csv")

# ---------- Styling ----------
st.markdown("""
    <style>
        .title {
            font-size: 36px;
            font-weight: 600;
            text-align: center;
            color: #4B8BBE;
            margin-bottom: 30px;
        }
        .summary-box {
            background-color: #f9f9f9;
            border: 1px solid #e1e1e1;
            padding: 20px;
            border-radius: 12px;
            box-shadow: 0px 2px 8px rgba(0,0,0,0.05);
            font-size: 18px;
            line-height: 1.6;
            white-space: pre-wrap;
        }
        .label {
            font-size: 18px;
            font-weight: 500;
            margin-bottom: 10px;
        }
    </style>
""", unsafe_allow_html=True)

# ---------- Title ----------
st.markdown('<div class="title">🧾 Customer Summary Viewer</div>', unsafe_allow_html=True)

# ---------- Dropdown ----------
selected_name = st.selectbox("Select a customer name:", data['name'])

# ---------- Summary Box ----------
if selected_name:
    intro = data.loc[data['name'] == selected_name, 'intro'].values[0]
    end = data.loc[data['name'] == selected_name, 'end'].values[0]
    summary = data.loc[data['name'] == selected_name, 'summary'].values[0]
    
    full_text = f"{intro} \n\n {end} \n\n {summary}"
    
    st.markdown('<div class="label">📄 Summary:</div>', unsafe_allow_html=True)
    st.markdown(f'<div class="summary-box">{full_text}</div>', unsafe_allow_html=True)
