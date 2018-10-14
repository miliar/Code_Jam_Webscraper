#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import sys

fin = open('alient.in','r')
L,D,N = [int(i) for i in fin.readline().split()]
data = [[ord(c)-97 for c in fin.readline()[:-1]] for i in range(D)]
for i in range(N):
    patt = []
    deep = False
    for c in fin.readline()[:-1]:
            if c == '(':
                patt.append([])
                deep = True
            elif c == ')':
                deep = False
            elif deep:
                patt[-1].append(ord(c)-97)
            else:
                patt.append([ord(c)-97])
                
    print "Case #"+str(i+1)+": "+str(sum([int(all([s[i] in patt[i]  for i in range(L)])) for s in data]))
