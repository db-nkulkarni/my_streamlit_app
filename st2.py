import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import streamlit as st

def cati_metrics():
    st.header ("BA - RR from immediate email send-out - Oct'22")
    df = pd.read_csv('cati_data.csv')
    panel =  df.loc[df['job'] == 'Panel']
    cati =  df.loc[df['job'] != 'Panel']

    # st.header("CATI stats:")
    st.subheader("Agreed for immediate email in CATI:")

    col1, col2, col3  = st.columns(3)

    with col1:
        st.metric('Panel', panel.shape[0])
    
    with col2:
        st.metric('CATI', cati.shape[0])

    with col3:
        st.metric('TOTAL', df.shape[0])
    # st.dataframe(cati)

    def pie():
        ## https://pythonwife.com/plotly-with-streamlit/
        state = cati['state'].value_counts()
        # converting to df and assigning new names to the columns
        state = pd.DataFrame(state)
        state = state.reset_index()
        state.columns = ['state', 'counts'] # change column names

        values = []
        fig = go.Figure(
        go.Pie(
        labels = state.state,
        values = state.counts,
        hoverinfo = "label+percent",
        textinfo = "percent"
    ))
        st.header("State distribution (for CATI recontact)")
        st.plotly_chart(fig)
    # pie()

    return cati, panel


def online_metrics():
    st.subheader("Completed Online survey:")
    # df=pd.read_csv('I&R2 online completes.csv', usecols=['tot_hour_diff', 'OnlineCompletionTime'])
    df=pd.read_csv('I&R2 online completes.csv')
    panel_online_completes =  df.loc[df['job'] == 'Panel']
    cati_online_completes =  df.loc[df['job'] != 'Panel']

    col1, col2, col3  = st.columns(3)

    st.subheader("Conversion rate:")

    with col1:
        st.metric('Panel', panel_online_completes.shape[0])
    
    with col2:
        st.metric('CATI', cati_online_completes.shape[0])

    with col3:
        st.metric('TOTAL', df.shape[0])

    col4, col5, col6  = st.columns(3)


    with col4:
        panel_RR = (panel_online_completes.shape[0] / panel.shape[0])  * 100
        st.metric('Panel', round(panel_RR, 1)) 
    
    with col5:
        cati_RR = (cati_online_completes.shape[0] / cati.shape[0])  * 100
        st.metric('CATI', round(cati_RR, 1))

    with col6:
        total_RR = ((panel_online_completes.shape[0] + cati_online_completes.shape[0]) / (panel.shape[0] + cati.shape[0])) * 100
        st.metric('TOTAL', round(total_RR, 1))



    # jobs = df['job'].unique()
    # jobs = st.sidebar.selectbox("Select job:", jobs)



    # # df=pd.read_csv('I&R2 online completes.csv', usecols=['tot_hour_diff', 'OnlineCompletionTime'])
    # st.header ("BA - Online completion tracking from immediate email send-out")
    # df=pd.read_csv('I&R2 online completes.csv')
    # df['Mycol'] =  df['sys_EndTime'].apply(pd.to_datetime)
    # # df_online['OnlineCompletionTime'] = df_online['Mycol'].dt.tz_localize('utc').dt.tz_convert('Australia/Sydney')
    # df['OnlineCompletionTime'] = df['Mycol'].dt.tz_localize('utc')
    # df['OnlineCompletionTime'] = df['OnlineCompletionTime'].dt.strftime('%d/%m/%Y')
    # df['OnlineCompletionTime']  = pd.to_datetime(df['OnlineCompletionTime'], errors='coerce')
    # df['OnlineCompletionTime'] = df['OnlineCompletionTime'].dt.strftime('%d/%m/%Y')
    # df2 = df.OnlineCompletionTime.value_counts().rename_axis('unique_values').to_frame('counts')
    # df2 = df2.sort_index(ascending=False)
    # # print(df2.columns)
    # # df2["unique_values"] = df2["unique_values"].astype('datetime64[ns]')
    # # df2['z'] = df2['unique_values'].apply(pd.to_numeric, errors='coerce')

    # # df2.sort_values(by='z', inplace=True)
    # print(df2)
    # # test = df2.sort_values('unique_values', ascending=True)
    # st.bar_chart(df2)
    
    # avg = df.tot_hour_diff.mean().round(1)

    # df = df.applymap(str)
    # jobs = df['job'].unique()
    # jobs = st.sidebar.selectbox("Select the job:", jobs)
    # fig = px.line(df[df['job'] == jobs], 
    # y = "tot_hour_diff", x = "OnlineCompletionTime", title = jobs)
    # st.metric('\nAvg completion hours after invite sending: ', str(avg))


    # # print(df.OnlineCompletionTime.value_counts().sort_index())

    # st.plotly_chart(fig)
    # # print(df.columns)
    # # st.line_chart(df)

cati, panel = cati_metrics()
online_metrics()















ind_dict = { 
        '1': 'Agriculture, Forestry and Fishing',
        '2': 'Construction',
        '3': 'Financial and Insurance Services',
        '4': 'Health Care and Social Assistance',
        '5': 'Manufacturing',
        '7': 'Retail Trade',
        '8': 'Transport, Postal and Warehousing',
        '9': 'Wholesale Trade',
        '10': 'Mining',
        '11': 'Electricity, Gas, Water and Waste Services',
        '12': 'Accommodation and Food Services',
        '13': 'Information, Media and Telecommunications',
        '14': 'Education and Training',
        '15': 'Arts and Recreation Services',
        '16': 'Other Services',
        '18': 'Rental, Hiring and Real Estate Services',
        '19': 'Professional, Scientific and Technical Services',
        '20': 'Administrative and Support Services'
    }
