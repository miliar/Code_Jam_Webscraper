#!/usr/bin/python3 -SOO
import math,string,itertools,fractions,re,array,bisect
from heapq import *
from collections import *

for cas in range(1,int(input())+1):
    n,m = map(int,input().strip().split())
    sz = sorted(map(int,input().strip().split()),reverse=True)
    taken = [False]*10000
    t = 0
    for i,x in enumerate(sz):
        if not taken[i]:
            t += 1
            taken[i] = True
            for j,y in enumerate(sz):
                if not taken[j] and x+y<=m:
                    taken[j] = True
                    break
    print('Case #%d: %d'%(cas,t))
    
    
