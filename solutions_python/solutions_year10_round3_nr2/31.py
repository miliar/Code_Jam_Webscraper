#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import sys

fin = open('load.in','r')
T = int(fin.readline()[:-1])
for t in range(T):
    L,P,C = [int(x) for x in fin.readline()[:-1].split()]
    i = 0
    j = L
    while j*C<P:
        i+=1
        j = j*C
    r = 0
    while i > 0:
        i = i/2
        r += 1
    print "Case #"+str(t+1)+": "+str(r)
