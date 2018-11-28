# -*- coding: utf-8 -*-
"""
Created on Sun Apr 30 12:42:31 2017

@author: Julien
"""

import os


chem="C:/CodeJam/ExoC"
FhIn="C-small-1-attempt1.in"
FhOut="Result"+FhIn



def solve(N,K,U,listCore):
    print('nex')
    listCore=sorted(listCore)
    sCore={s:listCore.count(s) for s in set(listCore)}
    if 1 not in sCore:
        sCore[1]=0
    
    print(sCore)
    niv=sorted(sCore.keys())
    
    while (U>0 and len(niv)>1):
        
        nextL=(niv[1]-niv[0])
       
        if U> sCore[niv[0]]*nextL:
            U-=sCore[niv[0]]*nextL
            sCore[niv[1]]+=sCore[niv[0]]
            del sCore[niv[0]]
        else:
            trained= U/sCore[niv[0]]
            U=0
            sCore[niv[0]+trained]=sCore[niv[0]]
            del sCore[niv[0]]
        niv=sorted(sCore.keys())
        print(sCore)
        U=round(U,4)
         
    r=1
    for i in sCore:
        r=r* pow(min(i,1),sCore[i])
    print(sCore)
    return r





with open(os.path.join(chem,FhIn),'r') as f:
    with open(os.path.join(chem,FhOut),'w') as fOut:
        C=int(f.readline())
        
        for c in range(C):
#            c=4
            [N,K]=[int(x) for x in f.readline().split()]
            [U]=[float(x) for x in f.readline().split()]
            core=[float(x) for x in f.readline().split()]

        
            r=solve(N,K,U,core)
            
            fOut.write("Case #"+str(c+1)+": " + str("%.6f" % r) +'\n')

