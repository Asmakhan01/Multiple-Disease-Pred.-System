# -*- coding: utf-8 -*-
"""
Created on Sun Feb 25 00:23:07 2024

@author: Asma
"""

import pickle
import streamlit as st
from stramlit_option_menu import option_menu

#loading the saved models

diabetes_model=pickle.load(open('C:/Users/Asma/Desktop/Multiple disease Prediction Syatem/saved_models/diabetes_model.sav','rb'))

heart_disease_model=pickle.load(open('C:/Users/Asma/Desktop/Multiple disease Prediction Syatem/saved_models/heart_model.sav','rb'))

parkinsons_disease_model=pickle.load(open('C:/Users/Asma/Desktop/Multiple disease Prediction Syatem/saved_models/parkinsons_model.sav','rb'))

#sidebar for navigation
with st.sidebar:
    selected= option_menu('Multiple Disease Prediction System',
                          ['Diabetes Prediction',
                           'Heart Disease Prediction',
                           'Parkinsons Prediction'],
                          default_index=0)

#Diabetes Prediction Page
if (selected=="Diabetes Prediction"):
    
    #page title
    st.title("Diabetes Prediction using ML")
#Heart Disease Prediction    
if (selected=="Heart Disease Prediction"):
    
    #page title
    st.title("Heart Disease Prediction using ML")
#Parkinsons Disease Prediction   
if (selected=="Parkinsons Disease Prediction"):
    
    #page title
    st.title("Parkinsons Disease Prediction using ML") 