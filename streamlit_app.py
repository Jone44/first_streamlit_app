import streamlit
import pandas

streamlit.title('My parents new sad dinner')

streamlit.header('Breakfast menu')

streamlit.text('Omega 3 ja mustkikka juduu')
streamlit.text('Muuta hyvvee')



streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')


my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')

streamlit.multiselect('pick some fruits:', list(my_fruit_list.index), ['Avocado', 'Strawberries'])

streamlit.dataframe(my_fruit_list)
