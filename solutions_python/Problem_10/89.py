# -* coding:utf-8 -*-
#! /usr/bin/python

import sys
import math
import numpy

import psyco

input=sys.stdin.read()
inList=input.split('\n')
N=int(inList.pop(0))


def f(P,K,L,frq):
    res = 0
    cost = 1
    cnt = 0
    for i in range(L):
        res += cost*frq[i]
        if (cnt+1) % K == 0:
            cost+=1
        cnt+=1
    return res


for i in range(N):

    P,K,L = [int(j) for j in inList.pop(0).split() ] 
    frq  = [int(j) for j in inList.pop(0).split() ] 

    frq.sort( lambda x,y: y-x )

    
    res = f(P,K,L,frq)


    print "Case #%d: %d"%(i+1, res)


    
