#Mbarkiimane_M1_BACHEV_11/12/2025
#Boudaoud Meryem
#Chekroun Hadjer
#Tahraoui Fatima
#Houari Kawther
# Biology Data Analysis Project
# Analyse de Séquences ADN avec Python et Pandas

import pandas as pd

# Données initiales
data = {
    'Séquence': ['ATGCGTACGTA', 'GCTAGCTAGGCC', 'ATGCGCGTAAGT', 
                 'TACGATCGTA', 'ATGAAAGGCTT', 'CGTACGTAGC', 'TTAACCGGAT'],
    'Longueur': [12, 12, 12, 10, 11, 10, 10],
    'Pourcentage GC': [50, 66.67, 58.33, 40, 45.45, 60, 50]
}

# 1) Créer et afficher le tableau avec pandas
df = pd.DataFrame(data)
print("1) TABLEAU INITIAL")
print(df)
print("\n")

# 2) Sélectionner et afficher uniquement la colonne "Longueur"
print("2) COLONNE 'LONGUEUR'")
print(df['Longueur'])
print("\n")

# 3) Filtrer les séquences dont la longueur est supérieure à 10
df_filtre = df[df['Longueur'] > 10]
print("3) SÉQUENCES AVEC LONGUEUR > 10")
print(df_filtre)
print("\n")

# 4) Calculer le pourcentage moyen de GC avec 3 chiffres après la virgule
moyenne_gc = round(df['Pourcentage GC'].mean(), 3)
print("4) POURCENTAGE MOYEN DE GC")
print(f"{moyenne_gc}%")
print("\n")

