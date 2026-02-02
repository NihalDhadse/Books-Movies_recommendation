import streamlit as st
import pickle
import numpy as np
import pandas as pd

st.set_page_config(
    page_title="Book Recommendation",
    layout="wide",
    page_icon="📚"
)

# ---------- BOOK THEME CSS ----------
st.markdown("""
<style>
.main {
    background: linear-gradient(120deg, #fdf6ec, #f0f7f4);
}
h1 {
    color: #1f4d4f;
    text-align: center;
    font-weight: 700;
}
.card {
    background: white;
    border-radius: 16px;
    padding: 10px;
    box-shadow: 0 8px 20px rgba(0,0,0,0.08);
    text-align: center;
}
.stButton>button {
    background: linear-gradient(90deg, #2ec4b6, #219ebc);
    color: white;
    border-radius: 30px;
    padding: 0.6em 1.8em;
    font-size: 16px;
    border: none;
}
</style>
""", unsafe_allow_html=True)

# ---------- LOAD DATA ----------
books = pickle.load(open('books.pkl', 'rb'))
pt = pickle.load(open('pt.pkl', 'rb'))
similarity_scores = pickle.load(open('similarity_scores.pkl', 'rb'))

# ---------- TITLE ----------
st.title("📚 Book Recommendation System")
st.markdown(
    "<p style='text-align:center; font-size:18px; color:#355f5b;'>Your next favorite book is waiting 📖</p>",
    unsafe_allow_html=True
)

# ---------- FUNCTION ----------
def recommend(book_name):
    index = np.where(pt.index == book_name)[0][0]
    similar_items = sorted(
        list(enumerate(similarity_scores[index])),
        key=lambda x: x[1],
        reverse=True
    )[1:6]

    names, authors, images = [], [], []
    for i in similar_items:
        temp_df = books[books['Book-Title'] == pt.index[i[0]]].drop_duplicates('Book-Title')
        names.append(temp_df['Book-Title'].values[0])
        authors.append(temp_df['Book-Author'].values[0])
        images.append(temp_df['Image-URL-M'].values[0])

    return names, authors, images

# ---------- UI ----------
selected_book = st.selectbox("📖 Choose a book", pt.index.values)

if st.button("✨ Find Similar Books"):
    names, authors, images = recommend(selected_book)

    cols = st.columns(5)
    for i in range(5):
        with cols[i]:
            st.markdown("<div class='card'>", unsafe_allow_html=True)
            st.image(images[i])
            st.subheader(names[i])
            st.caption(f"✍️ {authors[i]}")
            st.markdown("</div>", unsafe_allow_html=True)
