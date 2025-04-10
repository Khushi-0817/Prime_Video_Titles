import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
df = pd.read_csv("C:\\Users\\hp\\Downloads\\amazon_prime_titles.csv")
#display the dataset information
df.info()
df.describe()
df.shape
df.head()
df.nunique()
df.isnull().sum()
df.columns
df.drop_duplicates(inplace=True)
df.dropna(subset=['release_year', 'rating', 'country', 'listed_in'], inplace=True)


# bar chart showing top 10 most common genres
plt.figure(figsize=(10, 6))
top_genres = genres.value_counts().head(10) 
plt.bar(top_genres.index, top_genres.values, color='skyblue') 
plt.title('Top 10 Most Common Genres')
plt.xlabel('Genre')
plt.ylabel('Count')
plt.xticks(rotation=45)



# line chart showing no. of titles released per year
plt.figure(figsize=(10, 5))
yearly_counts = df.groupby('release_year').size().sort_index()
plt.plot(yearly_counts.index, yearly_counts.values, marker='o', linestyle='-', color='red') 
plt.title('Number of Titles Released per Year')
plt.xlabel('Year')
plt.ylabel('Number of Titles')
plt.grid()



# pie chart showing top 5 content ratings distribution
r_counts = df.groupby('rating').size().nlargest(5) 
plt.figure(figsize=(7, 7))
colors = sns.color_palette('pastel')
plt.pie(r_counts, labels=r_counts.index, autopct='%1.1f%%', colors=colors)
plt.title('Top 5 Content Ratings Distribution')



# histogram showing distribution of release years
plt.figure(figsize=(10, 5))
plt.hist(df['release_year'], bins=20, color='purple', edgecolor='black')  
plt.title('Distribution of Release Years')
plt.xlabel('Year')
plt.ylabel('Frequency')
plt.grid()



# donut chart showing Top 5 content ratings distribution
r_counts = df['rating'].value_counts().head(5)
plt.figure(figsize=(7, 7))
colors = sns.color_palette('pastel')
plt.pie(r_counts, labels=r_counts.index, autopct='%1.1f%%', colors=colors)
plt.gca().add_artist(plt.Circle((0, 0), 0.50, fc='white'))
plt.title('Top 5 Content Ratings Distribution')


# plotting a heatmap
df['duration'] = pd.to_numeric(df['duration'].str.replace(' min', '', regex=False), errors='coerce')
correlation_matrix = df.corr(numeric_only=True)
plt.figure(figsize=(6, 4))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f", linewidths=0.5)
plt.title("Correlation Heatmap")
