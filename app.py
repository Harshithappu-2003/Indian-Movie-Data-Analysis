## Objective

# 1. Design the page top header - Movie Data Analysis
# 2. Search option - person can search the movie (partial searches handling)
# 3. Add filters 
#     Genere 
#     Year 
#     Rating 
#     Votes
#     Language Filter 

# 4. Filters happened - Show the dataframe (Table on screen)

# 5. Vizualuzations - Selection Box 
#     Top 10 Movies based on Ratings. 
#     Top 10 Movies based on Votes 
#     Rating Distribution 
#     Top Genres by Count 
#     Votes vs Ratings


import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt
import streamlit as st
import plotly.express as px

## Load dataset 
def load_dataset():
    return pd.read_csv('output.csv')

df = load_dataset()

## Title 
st.title('Analysis of Indian Movies')

## Search Movie By Name 
st.subheader('Search Movie By Name')
search_name = st.text_input('Enter Movie Name either full or Partial')
if search_name:
    results = df[df['Movie Name'].str.contains(search_name, case=False)]
    if not results.empty:
        st.write(f'Found {len(results)} movies')
        st.dataframe(results[['Movie Name','Year','Timing(min)','Rating(10)','Votes','Genre','Language']])

    else:
        st.write('No Movies Found based on Query')


## Filters. 
st.sidebar.header("Filters")

## Filter By Genre
genre_filter = st.sidebar.multiselect("Select Genre", df['Genre'].unique(), default=[])

## Apply filters:
if genre_filter:
    df = df[df['Genre'].isin(genre_filter)]

## Filter By Language
language_filter = st.sidebar.multiselect("Select language", df['Language'].unique(), default=[])

## Apply filters:
if language_filter:
    df = df[df['Language'].isin(language_filter)]

## Year Slider filter 
year_range = st.sidebar.slider("Select Year Range", int(df['Year'].min()), int(df['Year'].max()), (1950,2025))
df = df[df['Year'].between(*year_range)]

## slider of ratings
## slider of votes 


## Display this filtered DF on screen 
st.subheader('Filtered Movies Data')
st.write(f'Found {len(df)} movies after filter')
st.dataframe(df)


### Data Visualization 
st.subheader('Visualizations.. ')
viz_selection = st.selectbox('Chose from given Analysis options', 
             ['Top 10 movies by Ratings',
              'Top 10 movies by Votes'])

if viz_selection == 'Top 10 movies by Ratings':
    filtered_df = df.sort_values(by = 'Rating(10)', ascending=False).head(10)
    st.write('TOP 10 Moves Based on Ratings')
    st.dataframe(filtered_df[['Movie Name','Year','Timing(min)','Rating(10)','Votes','Genre','Language']])
    st.write('BAR Chart : Top 10 Movies with Ratings')
    fig = px.bar(filtered_df, x = 'Movie Name', y = 'Rating(10)', title = 'Movies With Ratings')
    st.plotly_chart(fig)

elif viz_selection == 'Top 10 movies by Votes':
    filtered_df = df.sort_values(by = 'Votes', ascending=False).head(10)
    st.write('TOP 10 Moves Based on Votes')
    st.dataframe(filtered_df[['Movie Name','Year','Timing(min)','Rating(10)','Votes','Genre','Language']])
    st.write('BAR Chart : Top 10 Movies with Votes')
    fig = px.bar(filtered_df, x = 'Movie Name', y = 'Votes', title = 'Movies With Ratings')
    st.plotly_chart(fig)