# -*- coding: utf-8 -*-
"""
Created on Sun Apr 30 11:13:35 2017

@author: Julien
"""

import os
import math
from operator import itemgetter
from decimal import *

getcontext().prec=10


chem="C:/CodeJam/Exo A"
FhIn="A-large.in"
FhOut="Result"+FhIn


def calc(panList):
    cal=0
    for p in panList:
        cal+=(2*math.pi*p[0]*p[1])
    radius=[p[0] for p in panList]
    
    cal+=(math.pi*max(radius)*max(radius))
    return cal

def surf(pancake):
    return (2*math.pi*pancake[0]*pancake[1] + pancake[0]*pancake[0]*math.pi)

def hauteur(pancake):
    return (2*math.pi*pancake[0]*pancake[1])
    

def solve(N,K,panList):
    
    for i in range(N):
        panList[i].append(surf(panList[i]))
        panList[i].append(hauteur(panList[i]))
    
    test=True
    index=0
    panSurf=sorted(panList,key=lambda x: x[2],reverse=True)
#    print("Surf")
#    print(panSurf)
    while(test):
        rad=panSurf[index][0]
#        print(panSurf[index])
        panH=[panSurf[x] for x in range(len(panSurf)) if x!=index]
#        print(panH)
        if len(panH)>=K-1:
            panRes=[panSurf[index]]
            panH=sorted(panH,key=lambda x: x[3],reverse=True)
            for i in range(K-1):
                panRes.append(panH[i])
            test=False
        else:
            index+=1
        
    
    
    panH=sorted(panList,key=lambda x: x[2],reverse=True)
    
    
    
#    print(panRes)
    return calc(panRes)
    



with open(os.path.join(chem,FhIn),'r') as f:
    with open(os.path.join(chem,FhOut),'w') as fOut:
        C=int(f.readline())
        
        for c in range(C):
#            c=4
            [N,K]=[int(x) for x in f.readline().split()]
            panList=[]
            for p in range(N):
                panList.append([int(x) for x in f.readline().split()])
        
            r=solve(N,K,panList)
            
            fOut.write("Case #"+str(c+1)+": " + str("%.10f" % r) +'\n')
    