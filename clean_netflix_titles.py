import pandas as pd

df = pd.read_csv("netflix_titles.csv")
print("Original dataset shape:", df.shape)
print("\nFirst 5 rows before cleaning:\n", df.head())


df.dropna(subset=['title', 'type'], inplace=True)
df['country'].fillna('Unknown', inplace=True)
df['rating'].fillna('Unknown', inplace=True)
df['director'].fillna('Not Available', inplace=True)
df['cast'].fillna('Not Available', inplace=True)


df.drop_duplicates(inplace=True)


df['country'] = df['country'].str.strip().str.title()
df['type'] = df['type'].str.strip().str.title()
df['rating'] = df['rating'].str.strip().str.upper()


df['date_added'] = pd.to_datetime(df['date_added'], errors='coerce')


df.columns = df.columns.str.lower().str.replace(' ', '_')


df['release_year'] = df['release_year'].astype(int)


output_file = "netflix_titles_cleaned.csv"
df.to_csv(output_file, index=False)


print("\nCleaned dataset shape:", df.shape)
print("Cleaned data saved to:", output_file)
print("\nFirst 5 rows after cleaning:\n", df.head())
