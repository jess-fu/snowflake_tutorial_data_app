from isort import stream
import streamlit

# import pandas as pd
import requests
import snowflake.connector
from urllib.error import URLError

streamlit.stop()
# connect with Snowflake
my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("SELECT * from fruit_load_list")
my_data_row = my_cur.fetchall()
streamlit.header("snowflake table includes fruit")
streamlit.dataframe(my_data_row)

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
my_cur.execute("insert into fruit_load_list values ('pick some fruit')")


streamlit.header("Fruityvice Fruit Advice!")

fruit_choice = streamlit.text_input(
    "What fruit would you like information about?", "Kiwi"
)
streamlit.write("The user entered ", fruit_choice)

fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + fruit_choice)
# streamlit.text(fruityvice_response.json())

# change the fruityvice response to a dataframe?
fruityvice_normalized = pd.json_normalize(fruityvice_response.json())
# display the dataframe
streamlit.dataframe(fruityvice_normalized)

my_cur.execute("insert into fruit_load_list values ('get some fruit')")


fruit_add = streamlit.text_input("What fruit would you like to add?", "")
streamlit.write("The user entered ", fruit_add)

fruit_add_prompt = "Thanks for adding " + fruit_add
streamlit.text(fruit_add_prompt)
my_cur.execute("insert into fruit_load_list values ('add fruit')")
