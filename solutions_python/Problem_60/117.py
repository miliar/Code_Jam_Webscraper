#!/usr/bin/python2.6

import os, sys, math

file = open(sys.argv[1] , 'r')
nbr_testcases = int(file.readline())

for test in range(nbr_testcases):
    N, K, B, T = tuple([int(k) for k in file.readline().split()])
    pos = [int(k) for k in file.readline().split()]
    speed = [int(k) for k in file.readline().split()]
    dist = [B-v for v in pos]
    eta = [float(d)/float(s) for d, s in zip(dist, speed)]
    i = N-1
    arriving = []
    while i >= 0 and len(arriving) < K:
        if eta[i] <= T:
            arriving.append(i)
        i = i - 1
    if len(arriving) == K:
        count = 0
        for i in range(K):
            count = count + (N-1-arriving[i]-i)
        print "Case #"+str(test+1)+": "+str(count)
    else:
        print "Case #"+str(test+1)+": IMPOSSIBLE"

file.close()


