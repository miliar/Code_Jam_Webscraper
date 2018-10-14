#!/usr/bin/python3
# -*- coding: utf-8 -*-

from functools import reduce

def gcd2(v1,v2):
    if v1:
        return gcd2(v2%v1,v1)
    else:
        return v2

def gcd(*v):
    return reduce(gcd2,v)

fin = open("input.txt",'r')
fout = open("output.txt",'w')
C = int(fin.readline())
for i in range(C):
    v = list(map(int,fin.readline().split()))[1:]
    v2 = [abs(x-y) for x,y in zip(v[1:],v[:-1])]
    g = gcd(*v2)
    res = (g-(v[0]%g))%g
    print (i,res,g)
    print ("Case #%d: %d"%(i+1,res),file=fout)
