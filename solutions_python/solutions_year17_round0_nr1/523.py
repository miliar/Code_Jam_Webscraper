# -*- coding: utf-8 -*-
"""
Created on Fri Apr 10 21:34:08 2015

@author: Fred
"""



def qualifA0g(Liste,K):
    L=[]
    for j in range(len(Liste)):
       if Liste[j]=='+':
           L=L+[1]
       else:
           L=L+[0]
    
    # test en voulant finir à 0
    compteur=0
    for k in range(len(L)):
#        print L
        if L[k]==1:
            if k+K>len(L):
                return len(L)+1
            else:
                for j in range(k,k+K):
                    L[j]=(L[j]+1)%2
                compteur=compteur+1
    
    if 1 in L:
        return len(L)+1
    else:
        return compteur
        
    
def qualifA0d(Liste,K):
    L=[]
    for j in range(len(Liste)):
       if Liste[j]=='+':
           L=L+[1]
       else:
           L=L+[0]
    L=L[::-1]
    # test en voulant finir à 0
    compteur=0
    for k in range(len(L)):
#        print L
        if L[k]==1:
            if k+K>len(L):
                return len(L)+1
            else:
                for j in range(k,k+K):
                    L[j]=(L[j]+1)%2
                compteur=compteur+1
    
    if 1 in L:
        return len(L)+1
    else:
        return compteur
        


    
    # test en voulant finir à 1
def qualifA1g(Liste,K):
    L=[]
    for j in range(len(Liste)):
       if Liste[j]=='+':
           L=L+[1]
       else:
           L=L+[0]
    # test en voulant finir à 0
    compteur=0
    for k in range(len(L)):
#        print L
        if L[k]==0:
            if k+K>len(L):
                return len(L)+1
            else:
                for j in range(k,k+K):
                    L[j]=(L[j]+1)%2
                compteur=compteur+1
    
    if 0 in L:
        return len(L)+1
    else:
        return compteur    
    
    
def qualifA1d(Liste,K):
    L=[]
    for j in range(len(Liste)):
       if Liste[j]=='+':
           L=L+[1]
       else:
           L=L+[0]
    L=L[::-1]
    # test en voulant finir à 0
    compteur=0
    for k in range(len(L)):
#        print L
        if L[k]==0:
            if k+K>len(L):
                return len(L)+1
            else:
                for j in range(k,k+K):
                    L[j]=(L[j]+1)%2
                compteur=compteur+1
    
    if 0 in L:
        return len(L)+1
    else:
        return compteur      
    
def resultat(L,K):
#    res1=qualifA0g(L,K)
#    res2=qualifA0d(L,K)
    res3=qualifA1g(L,K)
    res4=qualifA1d(L,K)
    c=min([res3,res4])
    if c==len(L)+1:
        return 'IMPOSSIBLE'
    else:
        return c

import numpy as np

def main(ifn='A-large.in',ofn='output.txt'):
    with open(ifn) as inf:   # ouvre l'input et le renomme en inf
        with open(ofn,'w') as ouf:  # crée l'output dans lequel on va écrire
            noc = int(inf.readline().strip())  # permet de lire la 1ere ligne
                                               # en général le nbr de cas
                                               # le .strip() permet de virer les espace
            

#            print noc
            
            for tnoc in range(noc):          # boucle en fonction du nbr de cas

                ouf.write("Case #%d: " %(tnoc+1))   # case dans laquelle on écrit en sortie
                L=inf.readline().strip().split(' ')
                K=int(L[1])
                Liste=[]
                for k in range(len(L[0])):
                    Liste=Liste+[L[0][k]]
                
#                print Liste
                output=resultat(Liste,K)
                if output=='IMPOSSIBLE':
                    print Liste
                    print K
                if type(output)==int:
                    ouf.write("%d\n" %output) # car on a un entier
                else:
                    ouf.write("%s\n" %output)
main()

