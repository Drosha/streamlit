import http.client, urllib.parse
import streamlit as st
import pandas as pd

import plotly as px

fig = px.scatter_mapbox(df, lat="latitude", lon="longitude", zoom=3)

fig.update_layout(mapbox_style="open-street-map")
fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
st.plotly_chart(fig)
