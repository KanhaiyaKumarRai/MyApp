# -*- coding: utf-8 -*-
"""
Created on Sun Oct 24 11:41:35 2021

@author: mail4
"""

import streamlit as st
import numpy as np
import pandas as pd


st.write("""
         # My First APP
         Hello *world!*
         """)
         
data=np.arange(0,1000).reshape((200,5))
df=pd.DataFrame(data,columns=["A","B","C","D","E"])

st.line_chart(df)

a=df['A'].values
b=df['B'].values

st.write("Sum of A is")
a = st.slider('a')  # 👈 this is a widget
st.write(a, 'squared is', a * a)

b = st.button('b')  # 👈 this is a widget
st.write(b, 'sum is', b + b)

