import streamlit as st

# --- Page Config ---
st.set_page_config(page_title="Recommendation System", layout="wide")

# --- Hide sidebar, header, and footer ---
hide_streamlit_style = """
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    </style>
"""
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

# --- Custom CSS for styling ---
st.markdown("""
    <style>
    .title {
        font-size: 48px;
        color: #1f77b4;
        font-weight: bold;
        text-align: center;
        margin-bottom: 10px;
    }
    .subtitle {
        font-size: 20px;
        text-align: center;
        margin-bottom: 50px;
        color: #333333;
    }
    .stButton>button {
        width: 220px;
        height: 70px;
        font-size: 20px;
        font-weight: bold;
        border-radius: 15px;
        border: none;
        color: white;
        background: linear-gradient(90deg, #ff4b4b, #ff7b7b);
        transition: transform 0.2s;
    }
    .stButton>button:hover {
        transform: scale(1.05);
        cursor: pointer;
    }
    </style>
""", unsafe_allow_html=True)

# --- Title and subtitle ---
st.markdown('<div class="title">🎯 Recommendation System</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Choose what you want to explore:</div>', unsafe_allow_html=True)

# --- Buttons for navigation ---
col1, col2 = st.columns(2)

with col1:
    st.page_link("pages/book.py", label="📚 Book Recommendation")

with col2:
    st.page_link("pages/movies.py", label="🎬 Movie Recommendation")
