#!/usr/bin/python
# -*- coding: iso-8859-1 -*-
import sys
import math

with open(sys.argv[1], 'r') as f:
    for n in range(int(f.readline())):
        D, N = [int(i) for i in f.readline().split()]
        y = float('inf')
        for k in range(N):
            K,S = [float(i) for i in f.readline().split()]
            t = (float(D)-K)/S
            s = D/t
            if s < y:
                y = s
        print("Case #"+str(n+1)+": "+str(y))
