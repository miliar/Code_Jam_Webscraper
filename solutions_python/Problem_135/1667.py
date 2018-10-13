# -*- coding: utf-8 -*-
"""
Created on Sat Apr 12 13:35:45 2014

@author: Baplar
"""

with open("A-small-attempt0.in", "r") as fichier_entree:
    entree=fichier_entree.read()

liste_entree=entree.split("\n")

T=int(liste_entree[0])

i=0

liste_sortie=[]

while i<T:
    answer1=int(liste_entree[10*i+1])
    row1=liste_entree[10*i+1+answer1].split(" ")
    answer2=int(liste_entree[10*i+6])
    row2=liste_entree[10*i+6+answer2].split(" ")
    
    result=0
    for card in row1:
        if card in row2:
            result+=1
            solution=card
    if result==0:
        liste_sortie.append("Volunteer cheated!")
    elif result==1:
        liste_sortie.append(solution)
    elif result>1:
        liste_sortie.append("Bad magician!")
    
    i+=1

with open("Output.txt", "w") as fichier_sortie:
    for pos, sortie in enumerate(liste_sortie):
        chaine_sortie="Case #" + str(pos+1) + ": " + sortie
        if pos+1==T:
            fichier_sortie.write(chaine_sortie)
        else:
            fichier_sortie.write(chaine_sortie + "\n")
