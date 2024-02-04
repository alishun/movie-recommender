import pandas as pd

# Assuming 'tags.csv' is the file containing tags in the MovieLens dataset
tags_df = pd.read_csv('ml-25m/tags.csv')

# Group by movieId and calculate the average number of tags per movie
unique_tags = tags_df.groupby('movieId')['tag'].nunique()

# Display the result
print("Total unique tags:", tags_df['tag'].nunique())
print("Median number of tags per movie:", unique_tags.median())
print("Most number of tags per movie:", unique_tags.idxmax())