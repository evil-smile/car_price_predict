""" ayant deja fait l'analyse de notre donnees sur jupyter note notebook, nous 
allons directement ecrire une fonction qui prend entree les variables de notre
dataset et retour le prix du vehicule a travers notre modele de regression 
lineaire qu'ont a enregistrer avec joblib"""


#importation des bibliotheques 
import joblib
import streamlit as st
from sklearn.linear_model import LinearRegression

# lecture du modele enregistrer

st.write('le coeficient de la pente est :')