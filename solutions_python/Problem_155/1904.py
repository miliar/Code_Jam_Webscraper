'''
Created on 11/04/2015

@author: rogerrue
'''

import numpy as np
import random as rnd
from math import sqrt


def llegeixFitxer(fitxer="A-small-attempt0.in"):
    linies = [(lin.strip()).split("\n") 
              for lin in (open(fitxer).readlines())]
    # creo un diccionari amb una entrada per a cada web
    return linies

def liniesAnum(linies):
    tmp = []
    for lini in linies:
        for lin in lini:
            novalin = lin.strip().split(" ")
            novalin[0] = int(novalin[0])
            tmp.append(novalin)
    return tmp

linies = llegeixFitxer()
linies = liniesAnum(linies)
casos = linies[0][0]
for i in range(casos):
    j = i+1
    gent = 0
    falten = 0
    for k in range(len(linies[j][1])):
        sk = int(linies[j][1][k])
        if(k==0):
            gent += sk
        else:
            if(gent<k):
                afegeix = k-gent
                falten += afegeix
                gent += afegeix+sk
            else:
                gent += sk
    print "Case #"+str(j)+": "+str(falten)