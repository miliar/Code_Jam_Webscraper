#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr  8 11:10:50 2017

@author: Jacobo
"""

def create(line):
    tab=[]
    for i in line:
        if i=='+' or i=='-':
            tab.append(i)
    return tab

def flip(tab, i, largeur):
    for j in range(i,i+largeur):
        if tab[j]=='-':
            tab[j]='+'
        else:
            tab[j]='-'
    return tab

def solve(tab, largeur):
    cpt=0
    for j in range(0,len(tab)-largeur+1,1):
        if tab[j]=='-':
            tab=flip(tab,j,largeur)
            cpt+=1
    return cpt
            
def flipped(tab):
    for i in tab:
        if i =='-':
            return -1
    return 0

def getlargeur(line,tab):
    return int(line[len(tab)+1:-1])


res=open('./testlarge.sol','w')
    
route='./A-large.in'
#route='./1.test'
with open(route,'r') as file:
    lines=file.readlines()
    nombre=int(lines[0])
    for i in range(nombre):
        tab=create(lines[i+1])
        largeur=getlargeur(lines[i+1],tab)
        a=solve(tab, largeur)
        print(a,tab)
        aecrire='Case #'+str(i+1)+": "
        if(flipped(tab)==0):
            aecrire+=str(a)
        else:
            aecrire+="IMPOSSIBLE"
        aecrire+='\n'    
        res.write(aecrire)
        
        
res.close()