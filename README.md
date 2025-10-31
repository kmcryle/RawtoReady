## Project Background
RawtoReady is an interactive web app that simplifies data cleaning tasks for students, researchers, and analysts. Users can upload CSV datasets, apply multiple cleaning options (missing value handling, text normalization, duplicate removal, anomaly detection, etc.), and download a cleaned dataset.

## Features
Raw to Ready offers a seamless data-cleaning experience through a secure and user-friendly interface. It includes **user registration and login** with SHA-256 password hashing for security. Once logged in, users can **upload and preview their CSV datasets** before cleaning. The application provides a variety of **automated cleaning tools**—such as filling or dropping missing values, removing duplicates, standardizing column names, normalizing text, fixing date formats, validating email addresses, and applying fuzzy standardization to handle similar text values. It also detects numeric anomalies to help identify outliers.

After the cleaning process, users can view a **detailed Cleaning Summary Report** that presents statistics before and after cleaning. They can also **manage their Cleaning History**, with options to edit file names or delete past records. Finally, users can **download their cleaned dataset** as a CSV file for further analysis.

## Data Cleaning Workflow
1. Upload your CSV file.
2. Preview your raw dataset.
3. Choose cleaning options from the sidebar (what is suitable to your data, guidance is provided via tooltip).
4. Run Cleaning to automatically clean and standardize data.
5. View Results under:
   - Raw Data Preview
   - Cleaned Data Preview
   - Anomalies Detected
6. Summary Report will display statistics before and after cleaning.
7. Cleaning History page allows you to track, edit, or delete previous runs.
8. Download the cleaned and final CSV file.

## Login/Registration Workflow
User authentication is an **optional step**—guests can still use the app but won’t have access to personalized features such as cleaning history tracking.
- New users can register by clicking "Create Account" on the login register.
- Once the account is created, users can login page.
- Each user’s cleaning history is saved and can be viewed, edited, or deleted anytime.

## Tech Stack
- Frontend: Streamlit (Python framework for interactive web apps)
- Backend: Python (Pandas, NumPy)
- Database: SQLite
- Security: SHA-256 password hashing
- Other Libraries: FuzzyWuzzy, Scikit-learn, Regex

## Developers
RawtoReady is developed as part of SOftware Development final project to help users transform raw data into ready-to-analyze datasets efficiently. The developers are 3rd-year Data Science students, who personally created a web application they can use in their field/career. For more details about the project and/or proponents, below are the contact information:
- Gio Miguel R. Bihasa - gmrbihasa@mymail.mapua.edu.ph
- Pam Cassedy T. Dumangeng - pctdumangeng@mymail.mapua.edu.ph
- Kim Caryl H. Esperanza - kchesperanza@mymail.mapua.edu.ph
- Louella Josephine A. Ng - ljang@mymail.mapua.edu.ph
