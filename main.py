message = """
        __Select a page from the list below__
        """

import streamlit as st
st.set_page_config(layout = "wide") # optional

from stlib import overview
from stlib import insights
from stlib import predictionApp

with st.sidebar:
    page = st.selectbox('Pages:',['Overview','Insights', 'Heart Disease Prediction']) 

if page == 'Overview':
    overview.run()
elif page == 'Insights':
    insights.run()
else:
    predictionApp.run()