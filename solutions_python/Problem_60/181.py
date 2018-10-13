#!/usr/bin/python

import os
import sys
import math

infile = open(sys.argv[1])
case_num = int(infile.readline())

for ii in range(case_num):
    line = infile.readline()
    items = line.split(' ')
    N = int(items[0])
    K = int(items[1])
    B = int(items[2])
    T = int(items[3])
    line = infile.readline()
    items = line.split(' ')
    X = [int(t) for t in items]
    line = infile.readline()
    items = line.split(' ')
    V = [int(t) for t in items]
    could = [ (1 if X[i] + V[i] * T >= B else 0) for i in range(N)] 
    #print could
    total_swap = 0
    swap = 0
    success = 0
    could.reverse()
    for i in could:
        if i == 1:
            success += 1
            total_swap += swap
        else:
            swap += 1
        if success >= K:
            break
    if success == K:
        print 'Case #' + str(ii+1) + ':', total_swap
    else:
        print 'Case #' + str(ii+1) + ':', 'IMPOSSIBLE'

