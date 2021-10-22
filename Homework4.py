import streamlit as st
import pandas as pd
import altair as alt
from PIL import Image
import numpy as np
# st.write('Davis')
# Question 1
st.title('Welcome to Math 10')
# Q2
st.markdown("[Here] (https://github.com/) is a link to Chulin Tang's Github")
# Q3 upload files
uploaded_file = st.file_uploader(label='Upload a CSV file', type='CSV')
# Q4
# We want to convert the file to a panda df
# But error occurs if we don't have an uploaded file first
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    # If x is an empty string, make it numpy's nan'
    # otherwise leave x
    # df = df.applymap(lambda x: np.nan if x == '' else x)
    df = df.replace(' ', '')
    df = df.replace(",", '')

# Q6
# See Week3 Friday lec
# let c be the column name

    def can_be_numeric(c):
        try:
            pd.to_numeric(df[c])
            return True
        except:
            return False
    # make a list of all the columns that can be made numeric
    good_cols = [c for c in df.columns if can_be_numeric(c)]

# Q7
# Replace columns in df that can be made numeric with their numeric values
    df[good_cols] = df[good_cols].apply(pd.to_numeric, axis=0)
    # st.write(good_cols)
# Q8
# Select x-axis and y-axis from st.selectbox
    x_axis = st.selectbox('Choose an x-value', good_cols)
    y_axis = st.selectbox('Choose a y-value', good_cols)

# Q9
    row = st.slider('Select the rows you want plotted:', 0, len(df), (100, 600))

# Q10
    st.write(f'You are looking at row {row}')

# Q11
    cha = alt.Chart(df[row[0]:row[1]]).mark_circle().encode(
        x=x_axis,
        y=y_axis
    )
    st.altair_chart(cha, use_container_width=True)

# Q12
    # Import an image
    image = Image.open('Chris.png')
    st.image(image, caption='"Be the light of Data Science"')
