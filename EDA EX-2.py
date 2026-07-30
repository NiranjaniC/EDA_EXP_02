#!/usr/bin/env python
# coding: utf-8

# # EXPERIMENT - 2  Netflix Shows & Movies
# ## Name : Niranjani.C
# ## Registration Number : 212223220069

# In[16]:


import pandas as pd


# In[17]:


url = "https://raw.githubusercontent.com/allenkong221/netflix-titles-dataset/main/netflix_titles.csv"

df = pd.read_csv(url)


# In[18]:


print("Dataset Loaded Successfully!")


# In[19]:


print("First 5 Rows")
df.head()


# In[20]:


print("Last 5 Rows")
df.tail()


# In[21]:


print("Shape of Dataset:")
print(df.shape)


# In[22]:


print("Column Names")
print(df.columns)


# In[23]:


print("Data Types")
print(df.dtypes)


# In[24]:


print("Dataset Information")
df.info()


# In[25]:


print("Statistical Summary")
df.describe(include="all")


# In[26]:


print("Missing Values in Each Column")
print(df.isnull().sum())


# In[27]:


print("Percentage of Missing Values")

missing_percentage = (df.isnull().sum() / len(df)) * 100

print(missing_percentage.round(2))


# In[28]:


df["director"] = df["director"].fillna("Unknown")
df["country"] = df["country"].fillna("Unknown")
df["cast"] = df["cast"].fillna("Not Available")
df["rating"] = df["rating"].fillna("Not Rated")


# In[29]:


print("Missing Values After Filling")

print(df[["director", "country", "cast", "rating"]].isnull().sum())


# In[30]:


df_original = pd.read_csv(url)

clean_df = df_original.dropna(subset=["director", "country"])

print(clean_df.shape)


# In[31]:


print("Only Movie Records")

movies = df[df["type"] == "Movie"]

movies.head()


# In[32]:


print("Only TV Show Records")

tv_shows = df[df["type"] == "TV Show"]

tv_shows.head()


# In[33]:


print("Title, Country and Release Year")

df[["title", "country", "release_year"]].head(10)


# In[34]:


print("Rows 100 to 120")

df.iloc[100:121]


# In[35]:


print("Movies Released After 2018")

movies_after_2018 = df[
    (df["type"] == "Movie") &
    (df["release_year"] > 2018)
]

movies_after_2018.head(10)


# In[36]:


print("Titles Produced in India")

india_titles = df[
    df["country"].str.contains("India", na=False)
]

india_titles[["title", "country", "release_year"]].head(10)


# In[37]:


print("TV Shows from the United States")

us_tv = df[
    (df["type"] == "TV Show") &
    (df["country"].str.contains("United States", na=False))
]

us_tv[["title", "country"]].head(10)


# In[38]:


print("PG-13 Movies")

pg13_movies = df[
    (df["type"] == "Movie") &
    (df["rating"] == "PG-13")
]

pg13_movies[["title", "rating"]].head(10)


# In[39]:


print("Creating Title Length Column")

df["Title_Length"] = df["title"].str.len()

df[["title", "Title_Length"]].head()


# In[40]:


print("Creating Movie Age Column")

current_year = 2026

df["Movie_Age"] = current_year - df["release_year"]

df[["title", "release_year", "Movie_Age"]].head()


# In[41]:


print("Creating Is Recent Content Column")

df["Is_Recent_Content"] = df["release_year"] >= 2020

df[["title", "release_year", "Is_Recent_Content"]].head()


# In[42]:


print("Longest Title")

longest_title = df.loc[df["Title_Length"].idxmax()]

print(longest_title["title"])
print("Length:", longest_title["Title_Length"])


# In[43]:


print("Shortest Title")

shortest_title = df.loc[df["Title_Length"].idxmin()]

print(shortest_title["title"])
print("Length:", shortest_title["Title_Length"])


# In[44]:


print("Average Movie Age")

print(df["Movie_Age"].mean())


# In[45]:


print("Oldest Content")

oldest = df.loc[df["release_year"].idxmin()]

print(oldest[["title", "release_year"]])


# In[46]:


print("Newest Content")

newest = df.loc[df["release_year"].idxmax()]

print(newest[["title", "release_year"]])


# In[47]:


print("Titles in Uppercase")

df["Title_Upper"] = df["title"].str.upper()

df[["title", "Title_Upper"]].head(10)


# In[48]:


print("Titles in Lowercase")

df["Title_Lower"] = df["title"].str.lower()

df[["title", "Title_Lower"]].head(10)


# In[49]:


print("Length of Each Title")

df["Title_Length"] = df["title"].str.len()

df[["title", "Title_Length"]].head(10)


# In[50]:


print("Titles Containing 'Love'")

love_titles = df[
    df["title"].str.contains("Love", case=False, na=False)
]

love_titles[["title"]]


# In[51]:


print("Titles Containing 'Life'")

life_titles = df[
    df["title"].str.contains("Life", case=False, na=False)
]

life_titles[["title"]]


# In[52]:


print("Titles Starting with 'The'")

the_titles = df[
    df["title"].str.startswith("The", na=False)
]

the_titles[["title"]]


# In[53]:


print("Titles Ending with 'Story'")

story_titles = df[
    df["title"].str.endswith("Story", na=False)
]

story_titles[["title"]]


# In[54]:


print("Creating Primary Genre Column")

df["Primary_Genre"] = df["listed_in"].str.split(",").str[0]

df[["listed_in", "Primary_Genre"]].head(10)


# In[62]:


print("Number of Movies and TV Shows")

content_count = df.groupby("type").size()

print(content_count)


# In[63]:


print("Average Release Year by Content Type")

avg_release = df.groupby("type")["release_year"].mean()

print(avg_release)


# In[64]:


print("Number of Titles in Each Rating Category")

rating_count = df.groupby("rating").size()

print(rating_count)


# In[65]:


print("Top 10 Countries with Highest Number of Netflix Titles")

top_countries = df["country"].value_counts().head(10)

print(top_countries)


# In[66]:


print("Top 10 Directors by Number of Titles")

top_directors = df["director"].value_counts().head(10)

print(top_directors)


# In[67]:


print("Top 10 Most Common Genres")

genres = df["listed_in"].str.split(", ")

all_genres = genres.explode()

top_genres = all_genres.value_counts().head(10)

print(top_genres)


# In[68]:


print("Distribution of Movies and TV Shows Across Countries")

country_pivot = pd.pivot_table(
    df,
    index="country",
    columns="type",
    values="title",
    aggfunc="count",
    fill_value=0
)

country_pivot.head(10)


# In[69]:


print("Distribution of Movies and TV Shows by Release Year")

year_pivot = pd.pivot_table(
    df,
    index="release_year",
    columns="type",
    values="title",
    aggfunc="count",
    fill_value=0
)

year_pivot.tail(10)


# In[72]:


print("Creating MultiIndex using Country and Type")

multi_df = df.set_index(["country", "type"]).sort_index()

multi_df.head()


# In[73]:


print("Movies from India")

india_movies = multi_df.loc[("India", "Movie")]

india_movies.head(10)


# In[74]:


print("TV Shows from the United States")

us_tvshows = multi_df.loc[("United States", "TV Show")]

us_tvshows.head(10)


# In[75]:


print("Splitting Dataset into Movies and TV Shows")

movies = df[df["type"] == "Movie"]

tvshows = df[df["type"] == "TV Show"]

print("Movies:", movies.shape)
print("TV Shows:", tvshows.shape)


# In[76]:


print("Concatenating Movies and TV Shows")

combined_df = pd.concat([movies, tvshows])

combined_df.head()


# In[77]:


title_director = df[["title", "director"]]

title_country = df[["title", "country"]]

print(title_director.head())
print(title_country.head())


# In[78]:


print("Merging DataFrames using Title")

merged_df = pd.merge(
    title_director,
    title_country,
    on="title"
)

merged_df.head()


# In[81]:


df["date_added"] = pd.to_datetime(
    df["date_added"],
    errors="coerce"
)


# In[82]:


df["Year_Added"] = df["date_added"].dt.year

df["Month_Added"] = df["date_added"].dt.month_name()


# In[83]:


print("Movies and TV Shows Added Each Year")

year_added = df.groupby(["Year_Added", "type"]).size().unstack(fill_value=0)

year_added


# In[84]:


print("Movies and TV Shows Added Each Month")

month_added = df.groupby(["Month_Added", "type"]).size().unstack(fill_value=0)

month_added


# In[85]:


print("Country with the Highest Netflix Content")

top_country = df["country"].value_counts().idxmax()

print("Country:", top_country)


# In[86]:


print("Year with the Highest Number of Additions")

top_year = df["Year_Added"].value_counts().idxmax()

print("Year:", top_year)


# In[87]:


print("Most Common Rating")

common_rating = df["rating"].value_counts().idxmax()

print("Rating:", common_rating)


# In[88]:


print("Most Common Genre")

common_genre = (
    df["listed_in"]
    .str.split(", ")
    .explode()
    .value_counts()
    .idxmax()
)

print("Genre:", common_genre)


# In[89]:


print("Percentage of Movies and TV Shows")

content_percentage = (
    df["type"]
    .value_counts(normalize=True)
    * 100
)

print(content_percentage.round(2))


# In[90]:


print("\n========== SUMMARY REPORT ==========")

print("Country with Highest Netflix Content :", top_country)

print("Year with Highest Additions :", top_year)

print("Most Common Rating :", common_rating)

print("Most Common Genre :", common_genre)

print("\nPercentage of Movies and TV Shows")

print(content_percentage.round(2))


# In[ ]:




