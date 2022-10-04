import streamlit
import pandas as pd

streamlit.title("Healthy Dinner!")
streamlit.header("Breakfast Menu")
streamlit.text("Omega 3 & Blueburry Oatmeal")
streamlit.text("🥗Kale, Spinach & Rocket Smoothie")
streamlit.text("🥑🍞Avocado Toast")
streamlit.header("🍌🥭 Build Your Own Fruit Smoothie 🥝🍇")

my_fruit_list = pd.read_csv(
    "https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt"
)
streamlit.dataframe(my_fruit_list)
