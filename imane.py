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

# 5) Ajouter une colonne "Catégorie GC"
def categoriser_gc(pourcentage):
    if pourcentage > 55:
        return "Riche"
    elif 45 <= pourcentage <= 55:
        return "Moyen"
    else:
        return "Faible"

df['Catégorie GC'] = df['Pourcentage GC'].apply(categoriser_gc)
print("5) TABLEAU AVEC CATÉGORIE GC")
print(df)
print("\n")

# 6) Ajouter une colonne avec le nombre de 'G' dans chaque séquence
df['Nombre de G'] = df['Séquence'].apply(lambda x: x.count('G'))
print("6) TABLEAU AVEC NOMBRE DE G")
print(df)
print("\n")

# 7) Calculer l'écart-type du %GC et de la longueur des séquences
ecart_type_gc = round(df['Pourcentage GC'].std(), 3)
ecart_type_longueur = round(df['Longueur'].std(), 3)
print("7) ÉCART-TYPE")
print(f"Écart-type du %GC: {ecart_type_gc}")
print(f"Écart-type de la Longueur: {ecart_type_longueur}")
print("\n")

