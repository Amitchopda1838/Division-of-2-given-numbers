# -*- coding: utf-8 -*-
"""Untitled49.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1k82QB825GP21oMMZJjwVAkzfSisEh_6E
"""

import streamlit as st
string = "Division of 2 given numbers"
st.set_page_config(page_title=string, page_icon="🔍")

st.title('Division of 2 given numbers')
x1 = st.number_input('Enter a numerator')
x2 = st.number_input('Enter a denominator')
if (x2 != 0):
    division = x1 / x2
    st.write("The division of {0} and {1} is {2}".format(x1,x2,division))
else:st.write("please enter valid deniminator")