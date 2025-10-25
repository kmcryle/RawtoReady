#!/usr/bin/env python
# coding: utf-8

import streamlit as st
import pandas as pd

# ============================
# PAGE CONFIG
# ============================
st.set_page_config(page_title="Raw to Ready", page_icon="🧹", layout="wide")

# ============================
# HEADER
# ============================
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    st.image("logo.png", use_container_width=False)

st.markdown("""
<p style='font-size:15px; line-height:1.6; text-align:center;'>
Welcome to <b>Raw to Ready!</b> This tool makes data cleaning super simple — 
        no need to worry about messy spreadsheets. Just upload your CSV, choose what you’d like to fix, 
        and we’ll take care of the rest. In a few clicks, you’ll have a clean, ready-to-use dataset for your projects!
</p>
""", unsafe_allow_html=True)

# ============================
# LOGIN / REGISTER SECTION
# ============================
st.markdown("---")
st.markdown("## Login / Register")

col_login, col_register = st.columns(2)

with col_login:
    st.markdown("### 🔐 Login")
    st.text_input("Email", key="login_email")
    st.text_input("Password", type="password", key="login_password")
    st.button("Login", key="login_button")

with col_register:
    st.markdown("### 🧾 Register")
    st.text_input("Username", key="register_username")
    st.text_input("Email", key="register_email")
    st.text_input("Password", type="password", key="register_password")
    st.text_input("Confirm Password", type="password", key="register_confirm")
    st.button("Register", key="register_button")

# ============================
# SIDEBAR
# ============================
st.sidebar.image("logonobg.png", use_container_width=True)
st.sidebar.radio("Navigation", ["Home", "Login / Register"])

st.sidebar.markdown("### 📥 Step 1: Upload your Dataset")
st.sidebar.file_uploader("CSV Files are accepted", type=["csv"])

st.sidebar.markdown("### ⚙️ Step 2: Choose Cleaning Options")
st.sidebar.selectbox(
    "Missing Values",
    ["Fill with N/A", "Fill with Mean", "Fill with Median", "Fill by most common", "Drop Rows"]
)

with st.sidebar.expander("Advanced Options"):
    st.checkbox("Remove duplicates")
    st.checkbox("Standardize column names")
    st.checkbox("Normalize text")
    st.checkbox("Fix date formats")
    st.checkbox("Validate emails")
    st.checkbox("Fuzzy standardize values")
    st.checkbox("Detect anomalies")

st.sidebar.button("Run Cleaning")
st.sidebar.button("Download Cleaned CSV")

# ============================
# MAIN TABS
# ============================
tab1, tab2, tab3 = st.tabs(["Raw Data Preview", "Cleaned Data Preview", "Anomalies Detected"])

with tab2:
    st.dataframe(pd.DataFrame({"Sample": ["Cleaned data table placeholder"]}))

with tab3:
    st.dataframe(pd.DataFrame({"Anomaly Report": ["No anomalies detected (placeholder)"]}))

# ============================
# SUMMARY REPORT
# ============================
st.markdown("---")
st.markdown("## Summary Report")

col1, col2, col3, col4 = st.columns(4)
with col1:
    with st.container(border=True):
        st.markdown("<div style='font-size:22px;'>Total Rows</div>", unsafe_allow_html=True)
        st.markdown("<div style='font-size:40px;'>0</div>", unsafe_allow_html=True)

with col2:
    with st.container(border=True):
        st.markdown("<div style='font-size:22px;'>Null Values</div>", unsafe_allow_html=True)
        st.markdown("<div style='font-size:40px;'>0</div>", unsafe_allow_html=True)

with col3:
    with st.container(border=True):
        st.markdown("<div style='font-size:22px;'>Duplicates</div>", unsafe_allow_html=True)
        st.markdown("<div style='font-size:40px;'>0</div>", unsafe_allow_html=True)

with col4:
    with st.container(border=True):
        st.markdown("<div style='font-size:22px;'>Anomalies</div>", unsafe_allow_html=True)
        st.markdown("<div style='font-size:40px;'>0</div>", unsafe_allow_html=True)