import streamlit as st
import pickle
import joblib
import pandas as pd
import numpy as np
import os

st.title("Movie Recommendation System")

# ============================================
# FIX: Get the correct file paths automatically
# ============================================
# This gets the folder where THIS script is located
script_folder = os.path.dirname(os.path.abspath(__file__))

# Create full paths to your files
movies_file = os.path.join(script_folder, "movies.pickle")
similarity_file = os.path.join(script_folder, "similarity.joblib")

# ============================================
# Load your data (exactly like you originally did)
# ============================================
with open(movies_file, 'rb') as m:
    movies = pickle.load(m)

similarity = joblib.load(similarity_file)

# Get all movie names for dropdown
movies_names = movies['title'].values

# ============================================
# Your original recommendation function
# ============================================
def recommend(name_movie):
    # Find the index of the selected movie
    movie_index = movies[movies['title'] == name_movie].index[0]
    
    # Get similarity scores for this movie
    recommendations = similarity[movie_index]
    
    # Get top 5 similar movies (excluding the first one which is the movie itself)
    movie_list = sorted(enumerate(recommendations), reverse=True, key=lambda x: x[1])[1:6]
    
    # Collect the recommended movie titles
    recommended_movies = []
    for i in movie_list:
        recommended_movies.append(movies.iloc[i[0]].title)
    
    return recommended_movies

# ============================================
# Your original UI
# ============================================
name_movie = st.selectbox("Enter the movie name", movies_names)

if st.button("Recommend"):
    r = recommend(name_movie)
    st.write("Movies you'll also like:-")
    
    for i in r:
        st.write(i)