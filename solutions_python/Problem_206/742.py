#!/usr/bin/env python
import numpy as np


inFile = open('in.txt', 'r')
outFile = open('out.txt', 'w')
t = int(inFile.readline())
for test in range(1, t+1):
    D, N = map(int, inFile.readline().split(' '))
    maxTime = 0.0
    for i in range(N):
        K, S = map(int, inFile.readline().split(' '))
        t = max(0, D-K)/float(S)
        if t > maxTime:
            maxTime = t
    outFile.write("Case #{}: {}\n".format(test, D/maxTime))
