# -*- coding: utf-8 -*-
import math as mt
import networkx as nx
"""
Created on Sat Apr 22 22:48:20 2017

@author: DELL GAMING
"""
color = {0:"R",1:"Y",2:"B"}
re = {"R":0,"Y":1,"B":2}

t = int(input())
for i in range(1, t + 1):
    n, r, o, y, g, b, v = [int(x) for x in input().split(" ")]
#    print(y)
    ini = [r,y,b]
    store = [r,y,b]
#    print(store)
    small = {r:"R",y:"Y",b:"B"}
    co1 = store.index(max(store))
    A = color[co1]
    a = max(store)
#    print(A,a)
    store[store.index(max(store))] = -1
    co2 = store.index(max(store))
    B = color[co2]
    b = max(store)
#    print(B,b)
    store[store.index(max(store))] = -1
    co3 = store.index(max(store))
    C = color[co3]
    c = max(store)
    if A==B or B==C or C==A:
        print("boom")
        break
#    print(C,c)
    store[store.index(max(store))] = -1
    if b + c < a :
        print('Case #{}: IMPOSSIBLE'.format(i))
        continue
    out = []
    if b+c == a:
        for j in range(1, a + 1):
            if j <= b:
                out.extend([B,A])
            else:
                out.extend([C,A])
    else:
        for j in range(1, a + 1):
            if j <= a-(c-1):
                out.extend([B,A])
            elif j > a-(c - 1) and j <= b:
                out.extend([B,C,A])
            else:
                out.extend([C,A])
        out = out + [C]
        
    print('Case #{}: '.format(i),end='')
    for x in out:
        print(x,end='')
    print()