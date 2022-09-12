import streamlit as st
import pandas as pd
import numpy as np

def display_text():
    st.title ("this is the app title")
    st.header("this is the markdown")
    st.markdown("this is the header")
    st.subheader("this is the subheader")
    st.caption("this is the caption")
    st.code("x=2021")
    st.latex(r''' a+a r^1+a r^2+a r^3 ''')

def display_media():
    st.image(r"Check.jpg")

def input_widgets_selection():
    st.checkbox('yes')
    st.button('Click')
    st.radio('Pick your gender',['Male','Female'])
    st.selectbox('Pick your gender',['Male','Female'])
    st.multiselect('choose a planet',['Jupiter', 'Mars', 'neptune'])
    st.select_slider('Pick a mark', ['Bad', 'Good', 'Excellent'])
    st.slider('Pick a number', 0,50)

def input_widgets_text_boxes():
    st.number_input('Pick a number', 0,10)
    st.text_input('Email address')
    st.date_input('Travelling date')
    st.time_input('School time')
    st.text_area('Description')
    st.file_uploader('Upload a photo')
    st.color_picker('Choose your favorite color')

def display_message():
    st.success("You did it !")
    st.error("Error")
    # st.warnig("Warning")
    st.info("It's easy to build a streamlit app")
    st.exception(RuntimeError("RuntimeError exception"))


def display_sidebar():
    st.sidebar.title("You did it !")
    st.sidebar.button('Click')
    st.sidebar.radio('Gender', ['M', 'F'])

def line_chart():
    df= pd.DataFrame(
        np.random.randn(10, 2),
        columns=['x', 'y'])
    st.line_chart(df)
    # df=pd.read_csv('I&R2 online completes.csv', usecols=['tot_hour_diff', 'OnlineCompletionTime'])
    # df = df.applymap(str)
    # st.line_chart(df)

# display_text()
# display_media()
# input_widgets_selection()
# input_widgets_text_boxes()
# display_message()
# display_sidebar()
line_chart()
