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