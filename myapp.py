import streamlit as st
import numpy as np
import pandas as pd

st.header("My Streamlit App")

import streamlit as st
import pandas as pd
from sklearn import datasets
from sklearn.ensemble import RandomForestClassifier

st.write("""
# Simple Advertising Prediction App

This app predicts the **Advertising** type!
""")

st.sidebar.header('User Input Parameters')

def user_input_features():
    TV_ad = st.sidebar.slider('TV ad', 0.7, 296.4, 177)
    Radio_ad = st.sidebar.slider('Radio ad', 0, 49.6, 28.7)
    Newspaper_ad = st.sidebar.slider('Newspaper ad', 0.3, 114, 8.1)
    Sales_ad = st.sidebar.slider('Sales ad', 1.6, 27, 19.6)
    data = {'TV_ad': TV_ad,
            'Radio_ad': Radio_ad,
            'Newspaper_ad': Newspaper_ad,
            'Sales_ad': Sales_ad}
    features = pd.DataFrame(data, index=[0])
    return features

df = user_input_features()

st.subheader('User Input parameters')
st.write(df)

advertising = datasets.load_advertising()
X = advertising.data
Y = advertising.target

clf = RandomForestClassifier()
clf.fit(X, Y)

prediction = clf.predict(df)
prediction_proba = clf.predict_proba(df)

st.subheader('Class labels and their corresponding index number')
st.write(advertising.target_names)

st.subheader('Prediction')
st.write(advertising.target_names[prediction])
#st.write(prediction)

st.subheader('Prediction Probability')
st.write(prediction_proba)
