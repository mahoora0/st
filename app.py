import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

x = st.slider('Select a value')
st.write(x, 'squared is', x * x)

st.sidebar.title("this is written inside the sidebar")
st.sidebar.button("Click")
st.sidebar.radio("Pick your gender", ["Male", "Female"])

df = pd.DataFrame(
  np.random.randn(10,2),
  columns=['x', 'y'])
st.line_chart(df)

rand = np.random.normal(1, 2, size = 20)
fig, as = plt.subplots()
ax.hist(rand, bins=15) 
st.pyplot(fig)
