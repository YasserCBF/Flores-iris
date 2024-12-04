
import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


st.title("Explorador de Datos Iris con Streamlit")


iris = sns.load_dataset('iris')


st.sidebar.subheader("Datos de Iris")
st.sidebar.write(iris.head())


chart_type = st.sidebar.selectbox("Selecciona el tipo de gráfico", ["Histograma", "Diagrama de dispersión"])


if chart_type == "Histograma":

    feature = st.sidebar.selectbox("Selecciona la característica", iris.columns)
    fig, ax = plt.subplots(figsize=(8, 6))
    sns.histplot(iris[feature], kde=True, ax=ax)
    st.pyplot(fig)

else:

    feature_x = st.sidebar.selectbox("Selecciona la característica en el eje X", iris.columns)
    feature_y = st.sidebar.selectbox("Selecciona la característica en el eje Y", iris.columns)


    fig, ax = plt.subplots(figsize=(8, 6))


    sns.scatterplot(x=feature_x, y=feature_y, data=iris, hue='species', ax=ax)


    st.pyplot(fig)
