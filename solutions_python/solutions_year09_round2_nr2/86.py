#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import sys

fin = open('nextt.in','r')
T = int(fin.readline()[:-1])
for t in range(T):
    N = int(fin.readline()[:-1])
    N = [int(n) for n in list(str(N))]
    rev = sorted(N,reverse=True)
    if rev == N:
        N = sorted(N)
        m = min([n for n in N if n>0])
        N.remove(m)
        N = [m] + [0] + N
    else:
        i = len(N)-1
        while N[i] <= N[i-1]:
            i -= 1
        n = min([p for p in N[i:] if p > N[i-1]])
        k = sorted(N[i-1:])
        k.remove(n)
        N[i:] = k
        N[i-1] = n

    st = ""
    for n in N:
        st += str(n)
    print "Case #"+str(t+1)+": "+st
