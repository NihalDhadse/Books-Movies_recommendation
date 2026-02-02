import streamlit as st
import pickle
import pandas as pd
import requests

st.set_page_config(
    page_title="Movie Recommendation",
    layout="wide",
    page_icon="🎬"
)

# ---------- MOVIE THEME CSS ----------
st.markdown("""
<style>
.main {
    background: radial-gradient(circle at top, #1e293b, #020617);
    color: white;
}
h1 {
    color: #38bdf8;
    text-align: center;
    font-weight: 800;
}
.card {
    background: rgba(255,255,255,0.05);
    border-radius: 16px;
    padding: 10px;
    box-shadow: 0 0 20px rgba(56,189,248,0.3);
    text-align: center;
}
.stButton>button {
    background: linear-gradient(90deg, #e11d48, #f43f5e);
    color: white;
    border-radius: 30px;
    padding: 0.6em 1.8em;
    font-size: 16px;
    border: none;
    box-shadow: 0 0 15px rgba(225,29,72,0.8);
}
</style>
""", unsafe_allow_html=True)

# ---------- FUNCTIONS ----------
def fetch_poster(movie_id):
    response = requests.get(
        f"https://api.themoviedb.org/3/movie/{movie_id}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US"
    )
    data = response.json()
    return "https://image.tmdb.org/t/p/w500/" + data["poster_path"]

def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(
        list(enumerate(distances)),
        reverse=True,
        key=lambda x: x[1]
    )[1:6]

    names, posters = [], []
    for i in movies_list:
        movie_id = movies.iloc[i[0]].movie_id
        names.append(movies.iloc[i[0]].title)
        posters.append(fetch_poster(movie_id))

    return names, posters

# ---------- LOAD DATA ----------
movie_dict = pickle.load(open('movie_dict.pkl','rb'))
movies = pd.DataFrame(movie_dict)
similarity = pickle.load(open('similarity.pkl','rb'))

# ---------- TITLE ----------
st.title("🎬 Movie Recommendation System")
st.markdown(
    "<p style='text-align:center; font-size:18px; color:#94a3b8;'>Lights. Camera. Recommendations. 🍿</p>",
    unsafe_allow_html=True
)

# ---------- UI ----------
selected_movie_name = st.selectbox("🎞️ Choose a movie", movies["title"].values)

if st.button("🔥 Find Similar Movies"):
    names, posters = recommend(selected_movie_name)

    cols = st.columns(5)
    for i in range(5):
        with cols[i]:
            st.markdown("<div class='card'>", unsafe_allow_html=True)
            st.image(posters[i])
            st.subheader(names[i])
            st.markdown("</div>", unsafe_allow_html=True)
