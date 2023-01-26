import streamlit as st
import pandas as pd
import numpy as np
import joblib



def fonction_principal():

    # importation du modele
    df_load = joblib.load(filename='modele_1.pkl')

    # message d'acceuil
    st.title("BIENVENUE DANS MON APPLICATION DE PREDICTION DU PRIX DES VOITURES")

    st.subheader('par: JALIL KETOU, dévéloppeur')

    # fonction pour afficher le jeux de donnees
    @st.cache(persist=True)
    def load_data():
        data = pd.read_csv('CarPrice_Assignment.csv')
        return data

    # affichage du jeu de donnees
    df = load_data()
    df_sample = df.sample(10)
    st.subheader('Le jeu de donées sur les ventes des voitures')
    st.write(df_sample)

    # definition d'une fonction qui permettra de vendre nos voitures

    def principal():
        st.write(" ")
        type_client = st.radio("Bonjour monsieur/madame, voulez-vous vendre ou acheter une voiture ?",
                                ('vendeur', 'acheteur'))

        if type_client == 'acheteur':
            type_carburant = st.radio(
                "Entrer le type de carburant que vous voulez pour votre voture: 'essence' ou 'diesel'?", ('essence', 'diesel'))
            if type_carburant == 'essence':
                type_carburant = 1
            else:
                type_carburant = 0

            nombre_fenetre = st.radio("combien de fenêtre voulez-vous pour votre vehicule ? 2 ou 4 ? ", ('deux', 'quatre'))
            if nombre_fenetre == 'quatre':
                nombre_fenetre = 1
            else:
                nombre_fenetre = 0

            longueur_voiture = st.number_input("Quelle longueur voulez vous pour votre voiture (en cm) ? ",step=10)

            largeur_voiture = st.number_input("Quelle largeur voulez-vous pour votre voiture (en cm) ? ")

            hauteur_voiture = st.number_input("Quelle hauteur voulez-vous pour votre voiture (en cm) ?")

            poids_a_vide = st.number_input("Quel est poids a vide voulez-vous pour votre voiture (en kg) ?")

            parametres = {'fueltype': [type_carburant],
                          'doornumber': [nombre_fenetre],
                          'carlength': [longueur_voiture],
                          'carwidth': [largeur_voiture],
                          'carheight': [hauteur_voiture],
                          'curbweight': [poids_a_vide]}
            if st.button('prix')==True:
                df_test_model = pd.DataFrame(parametres)
                st.write("La voiture qui correspond a ces caracteristiques à pour prix", df_load.predict(df_test_model)[0],
                      '$')

        if type_client == 'vendeur':
            type_carburant = st.radio(
                "Entrer le type de carburant de le voiture que vous voulez vendre: 'essence' ou 'diesel'?", ('essence', 'diesel'))
            if type_carburant == 'essence':
                type_carburant = 1
            else:
                type_carburant = 0

            nombre_fenetre = st.radio("combien de fenêtre a votre vehicule ? 2 ou 4 ? ", ('deux', 'quatre'))
            if nombre_fenetre == 'quatre':
                nombre_fenetre = 1
            else:
                nombre_fenetre = 0

            longueur_voiture = st.number_input("Quelle longueur a votre voiture (en cm) ? ")

            largeur_voiture = st.number_input("Quelle largeur a votre voiture (en cm) ? ")

            hauteur_voiture = st.number_input("Quelle hauteur a votre voiture (en cm) ?")

            poids_a_vide = st.number_input("Quel est poids a vide a votre voiture (en kg) ?")

            parametres = {'fueltype': [type_carburant],
                          'doornumber': [nombre_fenetre],
                          'carlength': [longueur_voiture],
                          'carwidth': [largeur_voiture],
                          'carheight': [hauteur_voiture],
                          'curbweight': [poids_a_vide]}
            if st.button('prix')==True:
                df_test_model = pd.DataFrame(parametres)
                st.write("La voiture qui correspond a ces caracteristiques à pour prix", df_load.predict(df_test_model)[0],
                      '$')

    principal()
if __name__=="__main__":
    fonction_principal()