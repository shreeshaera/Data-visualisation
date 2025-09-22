import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

colors = ["#591717","#8F4609","#727D0A","#366909","#0E5139"]
#data cleaning
df = pd.read_csv("C:/Users/sribalaji/Downloads/netflix_titles.csv")
df = df.drop_duplicates()
df.fillna("NaN",inplace = True)
df['date_added'] = pd.to_datetime(df['date_added'],errors="coerce")
df['release_year'] = pd.to_numeric(df['release_year'],errors = "coerce")

#statistis with numpy and pandas
df["duration"] = pd.to_numeric(df["duration"].str.replace(" min","",regex = False),errors="coerce")
average = np.mean(df["duration"])
print(average)
count = df["type"].value_counts()
print(count)

#data visualisation with matplotlib
count.plot(kind = "bar", color=colors,width = 0.5)
plt.title("movie release count")
plt.show()

shows = df['release_year'].value_counts().sort_index()
shows.plot(kind = "line",color = "g")
plt.xlabel("Years")
plt.ylabel("Count")
plt.title("Shows released each year")
plt.legend()
plt.show()

df['listed_in'] = df['listed_in'].str.split(", ")
divided_genres = df.explode('listed_in')

genre = divided_genres['listed_in'].value_counts().head(5)
genre.plot(kind = "pie",autopct= "%2.1f%%",colors = colors)
plt.title("Top 5 genres")
plt.ylabel("")
plt.legend(bbox_to_anchor = (0,0.5),fontsize = 5)
plt.show()
