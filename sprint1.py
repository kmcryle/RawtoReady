#!/usr/bin/env python
# coding: utf-8

import streamlit as st
import pandas as pd

# ============================
# PAGE CONFIG
# ============================
st.set_page_config(page_title="Raw to Ready", page_icon="🧹", layout="wide")

# ============================
# SIDEBAR LOGO + NAVIGATION
# ============================
st.sidebar.image("logonobg.png", use_container_width=True)
menu = st.sidebar.radio("Navigation", ["Home", "Login / Register"])

# ============================
# HOME PAGE
# ============================
if menu == "Home":
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.image("logo.png", use_container_width=False)

    st.markdown("""
    <p style='font-size:15px; line-height:1.6;'>
     Welcome to <b>Raw to Ready!</b> This tool makes data cleaning super simple — 
        no need to worry about messy spreadsheets. Just upload your CSV, choose what you’d like to fix, 
        and we’ll take care of the rest. In a few clicks, you’ll have a clean, ready-to-use dataset for your projects!
    </p>
    """, unsafe_allow_html=True)

    # --- SIDEBAR FOR CLEANING ---
    st.sidebar.markdown("### 📥  Step 1: Upload your Dataset")
    uploaded_file = st.sidebar.file_uploader("CSV Files are accepted", type=["csv"])

    st.sidebar.markdown("### ⚙️ Step 2: Choose Cleaning Options")
    st.sidebar.caption("Select all options that apply. Hover over ❓ icons for tips.")

    fill_method = st.sidebar.selectbox(
        "Missing Values",
        ["Fill with N/A", "Fill with Mean", "Fill with Median", "Fill by most common", "Drop Rows"],
        help="💡 Tip: For small datasets, filling values is better. If your dataset is big, you can consider dropping the rows."
    )

    with st.sidebar.expander("Advanced Options"):
        st.checkbox("Remove duplicates", help="Removes exact duplicate rows.")
        st.checkbox("Standardize column names", help="Makes column names lowercase with underscores.")
        st.checkbox("Normalize text", help="Standardizes capitalization except for email fields.")
        st.checkbox("Fix date formats", help="Converts date formats to YYYY-MM-DD.")
        st.checkbox("Validate emails", help="Replaces invalid emails with `invalid@example.com`.")
        st.checkbox("Fuzzy standardize values", help="Groups similar text values (e.g., NYC, New York City).")
        st.checkbox("Detect anomalies", help="Flags unusual numeric values (possible outliers).")

    st.sidebar.markdown("#### Step 3: Apply Cleaning")
    st.sidebar.button("Run Cleaning")

    # --- MAIN CONTENT ---
    tab1, tab2, tab3 = st.tabs(["Raw Data Preview", "Cleaned Data Preview", "Anomalies Detected"])

    with tab1:
        st.markdown("### Raw Data Preview")
        if uploaded_file:
            df = pd.read_csv(uploaded_file)
            st.dataframe(df.head(10))
        else:
            st.info("Upload a CSV file to preview raw data.")

    with tab2:
        st.markdown("### Cleaned Data Preview")
        st.dataframe(pd.DataFrame({"Sample": ["Cleaned data table placeholder"]}))

    with tab3:
        st.markdown("### Anomalies Detected")
        st.dataframe(pd.DataFrame({"Anomaly Report": ["No anomalies detected (placeholder)"]}))

    # --- SUMMARY REPORT ---
    st.markdown("---")
    st.markdown("## Summary Report")

    rows_after = 0
    nulls_after = 0
    duplicates_after = 0
    anomalies_after = 0

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        with st.container(border=True):
            st.markdown("<div style='font-size:22px;'>Total Rows</div>", unsafe_allow_html=True)
            st.markdown(f"<div style='font-size:40px;'>{rows_after}</div>", unsafe_allow_html=True)
            st.progress(0)

    with col2:
        with st.container(border=True):
            st.markdown("<div style='font-size:22px;'>Null Values</div>", unsafe_allow_html=True)
            st.markdown(f"<div style='font-size:40px;'>{nulls_after}</div>", unsafe_allow_html=True)
            st.progress(0)

    with col3:
        with st.container(border=True):
            st.markdown("<div style='font-size:22px;'>Duplicates</div>", unsafe_allow_html=True)
            st.markdown(f"<div style='font-size:40px;'>{duplicates_after}</div>", unsafe_allow_html=True)
            st.progress(0)

    with col4:
        with st.container(border=True):
            st.markdown("<div style='font-size:22px;'>Anomalies</div>", unsafe_allow_html=True)
            st.markdown(f"<div style='font-size:40px;'>{anomalies_after}</div>", unsafe_allow_html=True)
            st.progress(0)

    st.download_button("Download Cleaned CSV", data=b"", file_name="cleaned_data.csv")

# ============================
# LOGIN / REGISTER PAGE
# ============================
elif menu == "Login / Register":
    st.markdown("---")
    st.markdown("## Login / Register")

    col_login, col_register = st.columns(2)

    # --- LOGIN SECTION ---
    with col_login:
        with st.container(border=True):
            st.markdown("### 🔐 Login")
            st.text_input("Email", key="login_email")
            st.text_input("Password", type="password", key="login_password")
            st.button("Login", key="login_button")

    # --- REGISTER SECTION ---
    with col_register:
        with st.container(border=True):
            st.markdown("### 🧾 Register")
            st.text_input("Username", key="register_username")
            st.text_input("Email", key="register_email")
            st.text_input("Password", type="password", key="register_password")
            st.text_input("Confirm Password", type="password", key="register_confirm")
            st.button("Register", key="register_button")