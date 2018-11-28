#!/usr/bin/python
# -*- coding: iso-8859-1 -*-
import sys
import math

# figures = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
# tidys =  ['1', '2', '3', '4', '5', '6', '7', '8', '9' ]
# prevs = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
# for i in range(16):
#     current = []
#     for tidy in prevs:
#         for j in figures:
#             if int(j) <= int(tidy[0]):
#                 current.append(j+tidy)
#     tidys.extend(current)
#     prevs=current

# print len(tidys)
# tidys.sort()
# print tidys


with open(sys.argv[1], 'r') as f:
    for n in range(int(f.readline())):
        N = [c for c in str(int(f.readline()))]
        for i in reversed(range(len(N)-1)):
            if N[i] > N[i+1]:
                N[i+1:] = ['9' for j in range(len(N)-i-1)]
                N[i] = str(int(N[i])-1)
        print("Case #"+str(n+1)+": "+str(int(''.join(N))))
        
