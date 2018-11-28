#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr  8 14:02:56 2017

@author: Jacobo
"""

def tidy(n):
    nombre=str(n)
    for i in range(len(nombre)-1):
        if int(nombre[i])>int(nombre[i+1]):
            return False
    return True

def latest(n):
    for i in range(n,0,-1):
        if tidy(i):
            return i
        
def launch2():
    file="./B-small-attempt0.in"
    out="./B-small-attempt0.out"
    with open(file,'r') as data:
        with open(out,'w') as outt:
            lignes=data.readlines()
            iterations=int(lignes[0][0:-1])
            for i in range(iterations):
                #Case #1: 129
                res=latest(int(lignes[i+1][0:-1]))
                ecrire='Case #'+str(i+1)+": "+str(res)+"\n"
                outt.write(ecrire)