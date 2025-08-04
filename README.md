# Netflix Data Cleaning with Python (Pandas)

# Overview
This project demonstrates how to clean and preprocess a raw Netflix dataset using Python and Pandas.  
The dataset contains missing values, inconsistent formats, and duplicates which were fixed through data cleaning steps.

# Steps Performed
1. Loaded the dataset using Pandas.
2. Handled missing values by dropping essential missing rows and filling others with defaults.
3. Removed duplicate records.
4. Standardized text fields (country, rating, etc.).
5. Converted `date_added` to datetime format.
6. Renamed column headers to be uniform.
7. Fixed data types (e.g., release_year to int).
8. Saved the cleaned dataset as `netflix_titles_cleaned.csv`.

# Files Included
- `clean_netflix_titles.py` – Python script for cleaning
- `netflix_titles.csv` – Raw dataset
- `netflix_titles_cleaned.csv` – Cleaned dataset
- `screenshots/` – Optional screenshots of the process
- `README.md` – Project documentation
