# -*- coding: utf-8 -*-
"""
Created on Fri Apr 10 21:34:08 2015

@author: Fred
"""



def qualifB(n):
    if len(n)==1:
       
        return n
    else:
        k=0
        init=int(n[k])
        L=[]
        while k<len(n) and int(n[k])>=init:
            init=int(n[k])
            k=k+1

            # plus dans l'ordre croissant. Il faut enlever 1 au précédent
                # et compléter par des 9 ensuite et tester si le précédent a aussi des un 1 ou pas...
        if k==len(n): # nombre n déjà rangé

            return n
        else: # k vaut au moins la valeur 1, auquel cas on a un problème au nombre d'indice k
            if n[k-1]!='1': # donc on recopie jusqu'à k-1, on diminue k-1 de 1 et on met des 9 après
                # on doit parcourir alors le nombre car si on a ABBBBBBC, diminuer le premier B déclassera le nombre...
                j=k-1
                while 0<=j and n[j]==n[k-1]:
                    j=j-1
#                print n
#                print j
#                print k
                # on a dans j le rang du premier B
                if j==-1:
                    return str(int(n[0])-1)+'9'*(len(n)-1)
                else:
#                print n[0:max(k-1,0)]+str(int(n[k-1])-1)+'9'*(len(n)-k)                
                    return n[0:(j+1)]+str(int(n[j+1])-1)+'9'*(len(n)-j-2)
    
            else: # donc le premier rang où ça a raté est de la forme XXXXX1Y donc forcément Y=0 et avant on a que des 1.
              
                return '9'*(len(n)-1)

import numpy as np

def main(ifn='B-large.in',ofn='output.txt'):
    with open(ifn) as inf:   # ouvre l'input et le renomme en inf
        with open(ofn,'w') as ouf:  # crée l'output dans lequel on va écrire
            noc = int(inf.readline().strip())  # permet de lire la 1ere ligne
                                               # en général le nbr de cas
                                               # le .strip() permet de virer les espace
            

#            print noc
            
            for tnoc in range(noc):          # boucle en fonction du nbr de cas

                ouf.write("Case #%d: " %(tnoc+1))   # case dans laquelle on écrit en sortie
                L=inf.readline().strip()
                resultat=int(qualifB(L))
                ouf.write("%d\n" %resultat) # car on a un entier


main()       


