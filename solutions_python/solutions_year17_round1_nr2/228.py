#!/usr/bin/env python
from math import *
from sys import *

numcases = int(stdin.readline())

for case in range(1,numcases+1):
    bounds = map(int, stdin.readline().split())
    N = bounds[0]
    P = bounds[1]
    Ri = map(int, stdin.readline().split())
    Qij = [] 
    for i in range(N):
        Qij.append(map(int, stdin.readline().split()))
    matches = [] 
    for i in range(N):
        matches.append([])
        for j in range(P):
            lowerbound = ceil(float(Qij[i][j])/(Ri[i]*1.1))
            upperbound = floor(Qij[i][j]/(Ri[i]*.9))
            if (lowerbound <= upperbound):
                matches[i].append((lowerbound,upperbound))
        matches[i].sort()

    kits = 0
    for i in range(len(matches[0])):
        rowPair = [-1]*(N-1)
        for j in range(1,N):
            for k in range(len(matches[j])):
                if matches[0][i][0] <= matches[j][k][1] and matches[j][k][0] <= matches[0][i][1]:
                    rowPair[j-1] = k
                    break
        if not (-1 in rowPair):
            kits += 1
            for g in range(len(rowPair)):
                del matches[g+1][rowPair[g]]

    print "Case #" + str(case) + ": " + str(kits)


