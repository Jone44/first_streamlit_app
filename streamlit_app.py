import streamlit
import pandas
import requests
import snowflake.connector
from urllib.error import URLError

streamlit.title('My moms new sad dinner')

streamlit.header('Breakfast menu')

streamlit.text('Omega 3 ja mustkikka juduu')
streamlit.text('Muuta hyvvee')



streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')


my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')

fruits_selected = streamlit.multiselect('pick some fruits:', list(my_fruit_list.index), ['Avocado', 'Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]





def get_fruityvice_data(this_fruit_choice):
  fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + fruit_choice)
  fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
  return fruityvice_normalized


streamlit.dataframe(fruits_selected)
streamlit.header('Fruityvice Fruit advice')
try:
  fruit_choice = streamlit.text_input('mitä hetelmää sä haluut?')
  if not fruit_choice:
    streamlit.error("Please select a fruit")
  else:
    back_from_function = get_fruityvice_data(fruit_choice)
    streamlit.dataframe(back_from_function)

except URLError as e:
  streamlit.error()

                                   
                                  
my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("SELECT * from fruit_load_list")
my_data_row = my_cur.fetchall()
streamlit.header("Hetelmälista sisältää:")
streamlit.dataframe(my_data_row)

fruit_choice2 = streamlit.text_input('What fruit to add?', 'kiwi')
streamlit.write('Adding', fruit_choice2)

