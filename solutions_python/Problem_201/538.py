# -*- coding: utf-8 -*-
"""
Created on Fri Apr 10 21:34:08 2015

@author: Fred
"""


# en fonction du rang de la personne, on veut savoir si elle sera dans une cabine du côté
# gauche ou du côté droit avec n>1

def cotepersonne(n):
    
    p=1
    puissance=1
    compteur2=0
    while n>=p:
        puissance=puissance*2
        p=p+puissance
        compteur2=compteur2+1
        # compte le nombre de personnes déjà passées



    # donc la on a n compris dans [p-puissance, p[
#    compteur=p-puissance-puissance/2 # nombre de personnes passées avant
    return [n-p+puissance+1,compteur2]


def eclatement(L):
    # on part d'une liste L=[[N1,k1],[N2,k2], etc] où k1 est le nbr de fois où N1 apparait
    dico={}
    for nombre in L:
        if nombre%2==1:
            newnomber=(nombre-1)/2
            if newnomber in dico:
                dico[newnomber]=dico[newnomber]+L[nombre]*2
            else:
                dico[newnomber]=L[nombre]*2
        else:
            newnomber1=(nombre)/2-1
            newnomber2=(nombre)/2
            if newnomber1 in dico:
                dico[newnomber1]=dico[newnomber1]+L[nombre]
            else:
                dico[newnomber1]=L[nombre]          
            if newnomber2 in dico:
                dico[newnomber2]=dico[newnomber2]+L[nombre]
            else:
                dico[newnomber2]=L[nombre]   
    return dico

# maintenant il n'y a plus qu'à éclater N le nombre de fois de la puissance

def eclatementrepete(N,s):
    
    niveau=cotepersonne(s-1)
#    print niveau
    p=niveau[1]
    dico={}
    dico[N]=1
    for k in range(p):
        dico=eclatement(dico)
    return dico


def tridico(dicoeclat,choix):
    # on va à présent renvoyer l'écart du nbr en position choix dans dicoeclat
    L=[]
    for nombre in dicoeclat:
        L=L+[nombre]
    L.sort()
    L=L[::-1]
    
    compteur=dicoeclat[L[0]] # maximum de dicoeclat    
    for j in range(0,len(L)):
        if compteur>=choix: # donc le choix 
            if L[j]%2==1:
                return ((L[j]-1)/2,(L[j]-1)/2)
            else:
                return (L[j]/2,L[j]/2-1)
        else:
            compteur=compteur+dicoeclat[L[j+1]]

def resultat(N,s):
    dicofin=eclatementrepete(N,s)
    niveau=cotepersonne(s-1)
    return tridico(dicofin,niveau[0])    


import numpy as np

def main(ifn='C-large.in',ofn='output.txt'):
    with open(ifn) as inf:   # ouvre l'input et le renomme en inf
        with open(ofn,'w') as ouf:  # crée l'output dans lequel on va écrire
            noc = int(inf.readline().strip())  # permet de lire la 1ere ligne
                                               # en général le nbr de cas
                                               # le .strip() permet de virer les espace
            

#            print noc
            
            for tnoc in range(noc):          # boucle en fonction du nbr de cas

                ouf.write("Case #%d: " %(tnoc+1))   # case dans laquelle on écrit en sortie
                L=inf.readline().strip().split(' ')
                N=int(L[0])
                s=int(L[1])
                resultatfin=resultat(N,s)
                affich=str(resultatfin[0])+' ' + str(resultatfin[1])
                ouf.write("%s\n" %affich)
main()

