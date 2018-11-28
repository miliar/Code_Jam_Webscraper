#!/usr/bin/python
#-*- coding: utf-8 -*- 


from sys import *


def ker(K):
## o número (k+1) tem que ser colocado na posição k%len(L)
    L=[K]
    start=0
    for k in range(K-1,0,-1):    
        #print k+1, "na pos", k, "mod", len(L)+1, "=", (k%len(L)+1), "de", L[0:start],"^", L[start+1:]
        L.insert( start%(len(L)), k)
        start = (start -k +1 )%len(L)
    return [start, L]

Ncasos = int(stdin.readline())

for caso in range(1,Ncasos+1):
        
    K = int(stdin.readline())
    Ir = stdin.readline()
    I = [int(k) for k in Ir.split()]
    I = I[1:]
    start, L = ker(K)
    print "Case #%d:"%caso,
    for i in I: 
        b = len(L)
        print L[ (i+start-1)%b],
    print
