import streamlit as st
import pandas as pd
from basic_ui import basic_recommender_ui
from watchlist import watchlist
import requests
from streamlit_lottie import st_lottie

st.set_page_config(
    layout="wide", page_title="Genre_Based", page_icon="images/icon1.png"
)

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

lottie_start = load_lottieurl("https://assets1.lottiefiles.com/packages/lf20_CTaizi.json")

#### CUSTOM CSS STYLING #####################################################################
style = f"""
<style>
.appview-container .main .block-container{{
        padding-top: 1rem;    }}
footer, header{{
    visibility: hidden;
}}
.movie-poster + div > .stButton, .movie-poster + div>.stButton>button{{
    font-size: 15px;
    width:100% !important;
    border-top:none;
    border-left: none;
    border-right:none;
    border-radius: 0px;
    background-color: transparent;
}}
.stButton, .stButton>button{{
    width: 100% !important;
}}
.movie-poster{{
    tranform: translateZ(10px);
}}
.movie-poster:hover{{
    transform: scale(1.03);
}}
</style>"""
st.markdown(style, unsafe_allow_html=True)
##############################################################################################

# INITIALIZING DATASETS ######################################################################
if "datasets" not in st.session_state:
    st.session_state["datasets"] = {
        "links": pd.read_csv(
            "Datasets/links.csv",
            index_col=[0],
            dtype={"movieId": int, "imdbId": str, "tmdbId": str, "imdb_link": str},
        ),
    }
if "watchlist" not in st.session_state:
    st.session_state["watchlist"] = watchlist()
################################################################################################

####### SETTING UP THE COMMON UI ELEMENTS ######################################################
if len(st.session_state["watchlist"].movies_list) > 0:
    with st.sidebar.expander("My Watchlist"):
        st.write(pd.Series(st.session_state["watchlist"].movies_list, name="Title"))

with st.container():
    left_column, right_column = st.columns(2)
with left_column:
         st.write("")
         st.title('MOVIE RECOMMENDER SYSTEM') 
with right_column:
         st_lottie(lottie_start, height=300,width=400, key="start")
     
st.sidebar.title("RECOMMEND ME")

    ### INITIALISE A BASIC RECOMMENDER UI RENDERING OBJECT ################
if "basic_recommender_ui" not in st.session_state:
        st.session_state["basic_recommender_ui"] = basic_recommender_ui(
            st.session_state["datasets"]["links"]
        )
    #######################################################################

st.session_state["basic_recommender_ui"].render()
##################################################################################################
