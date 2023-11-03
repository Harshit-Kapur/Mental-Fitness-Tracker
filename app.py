import streamlit as st
import pickle
import pandas as pd
import sklearn
st.title('Mental Fitness Tracker')
st.text('Fill the detail to check your mental fitness!')

Country=st.text_input('Enter your Country name ')
st.write(Country)
Code=st.text_input('Enter your Country code')
st.write(Code)
Year=st.number_input('Enter your Year',format="%d")
st.write(Year)
Schizophrenia=st.number_input('Enter your Schizophrenia rate in % ')
st.write(Schizophrenia)
Bipolar =st.number_input('Enter your Bipolar rate in %')
st.write(Bipolar)
Eating_disorder=st.number_input('Enter your Eating disorder rate')
st.write(Eating_disorder)
Anxiety_rate=st.number_input('Enter your Anxiety rate')
st.write(Anxiety_rate)
Drug_usage=st.number_input('Enter your Drug usage rate')
st.write(Drug_usage)
Depression=st.number_input('Enter your Depression rate')
st.write(Depression)
Alcohol_Consuming=st.number_input('Enter your Alcohol usage rate')
st.write(Alcohol_Consuming)
pickled_model = pickle.load(open(r"Mental-Fitness-Tracker/model.pkl", 'rb'))
df=pd.DataFrame({'Country':Country,'Code':Code,'Year':Year,'Schizophrenia':Schizophrenia,'Bipolar':Bipolar,'Eating':Eating_disorder,'Anxiety':Anxiety_rate,'Drug use':Drug_usage,'Depression':Depression,'Alcohol_use':Alcohol_Consuming},index=[0])
from sklearn.preprocessing import LabelEncoder
l=LabelEncoder()
for i in df.columns:
  if df[i].dtype=="object":
    df[i]=l.fit_transform(df[i])


button_clicked = st.button("Calculate")
if button_clicked:
    st.write("Button clicked!")
    predict=pickled_model.predict(df.values)
    st.write("Your Mental Fitness is {}%".format(predict[0]))

