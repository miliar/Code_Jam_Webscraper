# -*- coding: utf-8 -*-
"""
Created on Sat Apr 12 14:45:25 2014

@author: Baplar
"""

# Convert input file into a list
with open("Input.txt","r") as fichier_entree:
    entree=fichier_entree.read()
liste_entree=entree.split("\n")

def time(C, F, X, N):
    """Returns the time needed to get X cookies, given the price of a farm (C),
    the number of cookies a farm produces per second (F) and the number of
    farms bought (N)."""
    
    tps=0 # Elapsed time since the beginning of the production
    cps=2 # Cookie Per Seconds
    farms_owned=0 # Self-explanatory
    while farms_owned<N:
        tps+=C/cps
        cps+=F
        farms_owned+=1
    
    tps+=X/cps
    return tps
    

liste_sortie=[]

for i, chain in enumerate(liste_entree):
    if i==0:
        # Extract T
        liste_entree[0]=T=int(chain)
    if 0<i<T+1:
        # Transform each chain of the list into a list of parameters (C, F, X)
        liste_entree[i]=chain.split(" ")
        
        # Extract parameters
        C=float(liste_entree[i][0])
        F=float(liste_entree[i][1])
        X=float(liste_entree[i][2])
        
        # Increments the number of farms bought until a minimum time is reached
        solved=0        
        k=1
        result1=time(C,F,X,0)
        result2=time(C,F,X,1)
        
        while solved==0:
            if result1<=result2:
                # Minimum time is reached : output the value
                liste_sortie.append(round(result1,7))
                solved=1
            else:
                # Still decreasing, cuntinue buying farms
                k+=1
                result1=result2
                result2=time(C,F,X,k)

# Output the results in a file, with the correct format
with open("Output.txt", "w") as fichier_sortie:
    for pos, sortie in enumerate(liste_sortie):
        chaine_sortie="Case #" + str(pos+1) + ": " + str(sortie) # Concatenate chain
        if pos+1==T:
            # To not leave a blank line at the end of the file
            fichier_sortie.write(chaine_sortie)
        else:
            fichier_sortie.write(chaine_sortie + "\n")