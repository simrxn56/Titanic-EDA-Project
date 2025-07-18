import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('../data/train.csv')

df['Age'].fillna(df['Age'].median(), inplace=True)
df['Embarked'].fillna(df['Embarked'].mode()[0], inplace=True)
df.drop(['Cabin', 'Ticket', 'Name'], axis=1, inplace=True)

st.title('Titanic EDA Dashboard')

chart = st.selectbox("Select Chart", ['Survival Count', 'Survival by Gender', 'Age Distribution', 'Survival by Passenger Class'])

if chart == 'Survival Count':
    fig, ax = plt.subplots()
    sns.countplot(data=df, x='Survived')
    st.pyplot(fig)
elif chart == 'Survival by Gender':
    fig, ax = plt.subplots()
    sns.countplot(data=df, x='Sex', hue='Survived')
    st.pyplot(fig)
elif chart == 'Age Distribution':
    fig, ax = plt.subplots()
    sns.histplot(data=df, x='Age', hue='Survived', kde=True, bins=30)
    st.pyplot(fig)
else:
    fig, ax = plt.subplots()
    sns.countplot(data=df, x='Pclass', hue='Survived')
    st.pyplot(fig)
