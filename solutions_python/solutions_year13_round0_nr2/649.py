#!/usr/bin/python26
from __future__ import  print_function
import sys
sys.stdin = open("input.txt","r")
sys.stdout = open("output.txt","w")
t = input()
for n in range(t):
    x,y = map(int,raw_input().split())
    a = [list(map(int,raw_input().split())) for i in range(x)]
    vc= [a[i].count(1) for i in range(x) ]
    hc = [0] * y
    good = True
    for i in range(y):
        hc[i] = sum([(1 if a[j][i]==1 else 0) for j in range(x)])
    for i in range(x):
        for j in range(y):
            if a[i][j]==1:
                if vc[i]!=y and hc[j]!=x:
                    good = False
    print("Case #{0}: {1}".format(n+1,"YES" if good else "NO"))