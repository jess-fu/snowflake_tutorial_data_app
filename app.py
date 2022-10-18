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
my_fruit_list = my_fruit_list.set_index("Fruit")
fruits_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index))
fruits_to_show = my_fruit_list.loc[fruits_selected]

# Let's put a pick list here so they can pick the fruit they want to include
streamlit.dataframe(fruits_to_show)

streamlit.header("Fruityvice Fruit Advice!")
import requests

fruityvice_response = requests.get("https://fruityvice.com/api/fruit/watermelon")
streamlit.text(fruityvice_response.json())

# change the fruityvice response to a dataframe?
fruityvice_normalized = pd.json_normalize(fruityvice_response.json())
# display the dataframe
streamlit.dataframe(fruityvice_normalized)
