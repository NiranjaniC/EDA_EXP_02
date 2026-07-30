# Experiment 2: Netflix Dataset Analysis using Pandas

## Aim

To perform data analysis on the Netflix Titles dataset using Pandas by exploring the dataset, handling missing values, performing indexing and selection, creating new columns, applying string operations, grouping and aggregation, frequency analysis, pivot tables, hierarchical indexing, combining DataFrames, analyzing Netflix additions over time, and generating meaningful insights.

## Algorithm / Procedure

Step 1: Load and Explore the Dataset

Step 2: Analyze Missing Values

Step 3: Perform Data Indexing and Selection

Step 4: Create New Columns

Step 5: Perform Vectorized String Operations

Step 6: Perform Aggregation and Grouping

Step 7: Perform Frequency Analysis

Step 8: Create Pivot Tables

Step 9: Perform Hierarchical Indexing (MultiIndex)

Step 10: Combine DataFrames

Step 11: Analyze Netflix Additions Over Time

Step 12: Generate Summary Report

## Program
```
Developed By : Niranjani.C
Registration Number : 212223220069

import pandas as pd-

url = "https://raw.githubusercontent.com/allenkong221/netflix-titles-dataset/main/netflix_titles.csv"
df = pd.read_csv(url)

print("\nFirst 5 Rows")
print(df.head())

print("\nLast 5 Rows")
print(df.tail())

print("\nShape of Dataset")
print(df.shape)

print("\nColumn Names")
print(df.columns)

print("\nData Types")
print(df.dtypes)

print("\nDataset Information")
df.info()

print("\nStatistical Summary")
print(df.describe(include='all'))

df_original = df.copy()

print(df.isnull().sum())

print("\nMissing Value Percentage")
print(((df.isnull().sum()/len(df))*100).round(2))

df["director"] = df["director"].fillna("Unknown")
df["country"] = df["country"].fillna("Unknown")
df["cast"] = df["cast"].fillna("Not Available")
df["rating"] = df["rating"].fillna("Not Rated")

clean_df = df_original.dropna(subset=["director","country"])

print("\nClean Data Shape")
print(clean_df.shape)

movies = df[df["type"]=="Movie"]

tvshows = df[df["type"]=="TV Show"]

print("\nSelected Columns")
print(df[["title","country","release_year"]].head())

print("\nRows 100-120")
print(df.iloc[100:121])

print("\nMovies Released After 2018")
print(df[(df["type"]=="Movie") &
         (df["release_year"]>2018)].head())

print("\nTitles Produced in India")
print(df[df["country"].str.contains("India",na=False)].head())

print("\nTV Shows from United States")
print(df[(df["type"]=="TV Show") &
         (df["country"].str.contains("United States",na=False))].head())

print("\nPG-13 Movies")
print(df[(df["type"]=="Movie") &
         (df["rating"]=="PG-13")].head())

df["Title_Length"] = df["title"].str.len()

df["Movie_Age"] = 2026 - df["release_year"]

df["Is_Recent_Content"] = df["release_year"] >= 2020

print("\nLongest Title")
print(df.loc[df["Title_Length"].idxmax(),"title"])

print("\nShortest Title")
print(df.loc[df["Title_Length"].idxmin(),"title"])

print("\nAverage Movie Age")
print(df["Movie_Age"].mean())

print("\nOldest Content")
print(df.loc[df["release_year"].idxmin(),["title","release_year"]])

print("\nNewest Content")
print(df.loc[df["release_year"].idxmax(),["title","release_year"]])

df["Title_Upper"] = df["title"].str.upper()

df["Title_Lower"] = df["title"].str.lower()

df["Primary_Genre"] = df["listed_in"].str.split(",").str[0]

print("\nTitles containing Love")
print(df[df["title"].str.contains("Love",case=False,na=False)][["title"]])

print("\nTitles containing Life")
print(df[df["title"].str.contains("Life",case=False,na=False)][["title"]])

print("\nTitles starting with The")
print(df[df["title"].str.startswith("The",na=False)][["title"]])

print("\nTitles ending with Story")
print(df[df["title"].str.endswith("Story",na=False)][["title"]])

print(df.groupby("type").size())

print(df.groupby("type")["release_year"].mean())

print(df.groupby("rating").size())

print("\nTop 10 Countries")
print(df["country"].value_counts().head(10))

print("\nTop 10 Directors")
print(df["director"].value_counts().head(10))

print("\nTop 10 Genres")
genres = df["listed_in"].str.split(", ").explode()
print(genres.value_counts().head(10))

country_pivot = pd.pivot_table(
    df,
    index="country",
    columns="type",
    values="title",
    aggfunc="count",
    fill_value=0
)

print(country_pivot.head())

year_pivot = pd.pivot_table(
    df,
    index="release_year",
    columns="type",
    values="title",
    aggfunc="count",
    fill_value=0
)

print(year_pivot.tail())

multi_df = df.set_index(["country","type"]).sort_index()

print(multi_df.loc[("India","Movie")].head())

print(multi_df.loc[("United States","TV Show")].head())

combined_df = pd.concat([movies,tvshows])

title_director = df[["title","director"]]

title_country = df[["title","country"]]

merged_df = pd.merge(title_director,title_country,on="title")

print(merged_df.head())

df["date_added"] = pd.to_datetime(df["date_added"],format="mixed",errors="coerce")

df["Year_Added"] = df["date_added"].dt.year

df["Month_Added"] = df["date_added"].dt.month_name()

print(df.groupby(["Year_Added","type"]).size().unstack(fill_value=0))

print(df.groupby(["Month_Added","type"]).size().unstack(fill_value=0))

print("\n========== STEP 12: SUMMARY REPORT ==========")

print("Country with Highest Content:",
      df["country"].value_counts().idxmax())

print("Year with Highest Additions:",
      df["Year_Added"].value_counts().idxmax())

print("Most Common Rating:",
      df["rating"].value_counts().idxmax())

print("Most Common Genre:",
      df["listed_in"].str.split(", ").explode().value_counts().idxmax())

print("\nPercentage of Movies and TV Shows")
print((df["type"].value_counts(normalize=True)*100).round(2))

```

## Output

<img width="958" height="624" alt="image" src="https://github.com/user-attachments/assets/553c0025-b2f2-45b3-9eb1-a1f5772aa66c" />
<img width="952" height="732" alt="image" src="https://github.com/user-attachments/assets/b6aeb6ef-2356-4fd0-aa56-d337ca0ded3e" />
<img width="952" height="808" alt="image" src="https://github.com/user-attachments/assets/429d26ee-b874-4a54-a572-0e43d5784e12" />
<img width="950" height="577" alt="image" src="https://github.com/user-attachments/assets/402092a2-dd90-44c9-bf76-fb7ca1bcf2aa" />
<img width="958" height="661" alt="image" src="https://github.com/user-attachments/assets/9a0a0132-c5a3-4f7a-9fbd-f14318df6722" />
<img width="954" height="816" alt="image" src="https://github.com/user-attachments/assets/81fb0a45-3edd-49ca-a003-68420b6dcc89" />
<img width="956" height="848" alt="image" src="https://github.com/user-attachments/assets/062cd8ae-78be-4367-9d4b-312a85a8dbae" />
<img width="955" height="768" alt="image" src="https://github.com/user-attachments/assets/ef3de3e4-59ed-4bd1-a2d5-87ce3ffda8e9" />
<img width="956" height="816" alt="image" src="https://github.com/user-attachments/assets/5e4d30e2-26ef-4bea-b516-1d9c02d4e52a" />
<img width="958" height="628" alt="image" src="https://github.com/user-attachments/assets/d579ca14-704b-45dd-b518-b52b18a29d06" />
<img width="952" height="857" alt="image" src="https://github.com/user-attachments/assets/8bc0c112-368f-40fd-b60c-8e38bc877610" />
<img width="955" height="860" alt="image" src="https://github.com/user-attachments/assets/abae49a4-2c11-4045-b8ab-28131ad438f7" />
<img width="954" height="743" alt="image" src="https://github.com/user-attachments/assets/514b5419-340a-4185-96c0-7f1fa98b4010" />
<img width="955" height="852" alt="image" src="https://github.com/user-attachments/assets/0306620b-cf02-42f0-8d20-9a432507b280" />
<img width="963" height="683" alt="image" src="https://github.com/user-attachments/assets/c147a937-6d19-4985-a924-92310569ba28" />
<img width="952" height="739" alt="image" src="https://github.com/user-attachments/assets/5014cc85-44b3-4214-a0b8-b17c887c0227" />
<img width="952" height="857" alt="image" src="https://github.com/user-attachments/assets/bd96cfd6-1459-41a9-947b-e1e62128cfd4" />
<img width="949" height="668" alt="image" src="https://github.com/user-attachments/assets/5836ab75-10c6-47b3-b9a3-36f26468a163" />
<img width="953" height="872" alt="image" src="https://github.com/user-attachments/assets/c372d450-6cf5-4074-b606-68960d8ecd1b" />
<img width="654" height="269" alt="image" src="https://github.com/user-attachments/assets/ebf7c086-3914-44d4-a648-9d3764ac8426" />

## Result

The Netflix dataset was successfully analyzed using Pandas. The experiment demonstrated various data analysis techniques such as data exploration, missing value handling, indexing, filtering, string operations, aggregation, pivot tables, hierarchical indexing, DataFrame combination, time-based analysis, and summary reporting. Meaningful insights regarding Netflix content distribution, ratings, genres, countries, and release trends were successfully obtained.
