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



