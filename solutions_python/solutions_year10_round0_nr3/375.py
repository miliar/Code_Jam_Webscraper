#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import sys

def rotate(l):
    l.append(l[0])
    l[0:1] = []

fin = open('theme.in','r')
fout = open('theme.out','w')
T = int(fin.readline())
for t in range(T):
    R,k,N = [int(i) for i in fin.readline().split()]
    g = [int(i) for i in fin.readline().split()]
    i = 0
    m = 0
    r = 0
    money = [-1 for i in range(N)]
    rounds = [-1 for i in range(N)]
    while r<R:
        seats = 0
        j = 0
        while g[0]+seats <= k and j<N:
            j+=1
            seats += g[0]
            rotate(g)
            rotate(money)
            rotate(rounds)
        if seats == 0:
            print "Case #"+str(t+1)+": "+str(m)
        r += 1
        m += seats
        if money[0] == -1:
            money[0] = m
            rounds[0] = r
        else:
            d = (R-r)/(r-rounds[0])
            m += d*(m-money[0])
            r += d*(r-rounds[0])

        
    fout.write("Case #"+str(t+1)+": "+str(m)+"\n")
fout.close()
fin.close()
