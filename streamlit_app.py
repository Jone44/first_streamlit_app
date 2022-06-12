import streamlit
import pandas
import requests

streamlit.title('My moms new sad dinner')

streamlit.header('Breakfast menu')

streamlit.text('Omega 3 ja mustkikka juduu')
streamlit.text('Muuta hyvvee')



streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')


my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')

fruits_selected = streamlit.multiselect('pick some fruits:', list(my_fruit_list.index), ['Avocado', 'Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]

streamlit.dataframe(fruits_selected)


streamlit.header('Fruityvice Fruit advice')
frit_choice = streamlit.text_input('mitä hetelmää sä haluut?', 'kiwi')
streamlit.write('The user entered', fruit_choise)

fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + 'kiwi)
fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
streamlit.dataframe(fruityvice_normalized)
                                   
                                  
