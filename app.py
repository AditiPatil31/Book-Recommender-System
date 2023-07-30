import streamlit as st

import pickle
import numpy as np

def recommend_book(book_name):
    book_id = np.where(book_pivot.index == book_name)[0][0]
    distances, suggestions = model.kneighbors(book_pivot.iloc[book_id, :].values.reshape(1, -1), n_neighbors=6)
    suggestions = suggestions.flatten().tolist()
    for i in range(1, len(suggestions)):
            st.write(book_pivot.index[suggestions[i]])


model = pickle.load(open('model.pkl', 'rb'))
book_pivot = pickle.load(open('book_pivot.pkl', 'rb'))

st.title("Book Recommender System")

book_name = st.text_input("Enter the book name")



if st.button('recommend'):
    recommend_book(book_name)
