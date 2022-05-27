import streamlit as st
import pickle
import pandas as pd
import requests
from PIL import Image
from streamlit_lottie import st_lottie


#Setting the Page Configuration
img = Image.open('icon1.png')
st.set_page_config(page_title='TitleBased' , page_icon=img , layout="centered",initial_sidebar_state="expanded")



def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

lottie_start = load_lottieurl("https://assets2.lottiefiles.com/packages/lf20_khzniaya.json")

def fetch_poster(movie_id):
    response = requests.get('https://api.themoviedb.org/3/movie/{}?api_key=f4843b71ceb62352b7da17574f294c63&language=en-US'.format(movie_id))
    data = response.json()
    return "https://image.tmdb.org/t/p/w500/"+data['poster_path']


def recommend(movie):
        movie_index = movies[movies['title'] == movie].index[0]
        distances = similarity[movie_index]
        movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

        recommended_movies = []
        recommended_movies_posters = []
        for i in movies_list:
            movie_id = movies.iloc[i[0]].movie_id
            recommended_movies.append(movies.iloc[i[0]].title)
            # fetch poster
            recommended_movies_posters.append(fetch_poster(movie_id))
        return recommended_movies,recommended_movies_posters

movies_dict = pickle.load(open('movie_dict.pkl','rb'))
movies = pd.DataFrame(movies_dict)

similarity = pickle.load(open('similarity.pkl','rb'))

with st.container():
    left_column, right_column = st.columns(2)
with left_column:
    st.write("")
    st.title('MOVIE RECOMMENDER SYSTEM') 
with right_column:
    st_lottie(lottie_start, height=300,width=400, key="start")

selected_movie_name = st.selectbox(
'SELECT A MOVIE:',
movies['title'].values)

if st.button('Recommend Me'):
    names,posters = recommend(selected_movie_name)

    col1,col2,col3,col4,col5 = st.columns(5)
    with col1:
        st.text(names[0])
        st.image(posters[0])
    with col2:
        st.text(names[1])
        st.image(posters[1])
    with col3:
        st.text(names[2])
        st.image(posters[2])
    with col4:
        st.text(names[3])
        st.image(posters[3])
    with col5:
        st.text(names[4])
        st.image(posters[4])


