#!/usr/bin/python
# -*- coding: iso-8859-1 -*-
import sys
import math

with open(sys.argv[1], 'r') as f:
    for n in range(int(f.readline())):
        string, integer = f.readline().split()
        string = [c for c in string]
        K = int(integer)
        flips = 0
        for i in range(len(string)-K+1):
            if string[i] == '-':
                flips += 1
                for j in range(K):
                    string[i+j] = '-' if string[i+j] == '+' else '+'
        if '-' in string[-K:]:
            print("Case #"+str(n+1)+": IMPOSSIBLE")
        else:
            print("Case #"+str(n+1)+": "+str(flips))
