#!/usr/bin/python2.6

import os, sys, math

file = open(sys.argv[1] , 'r')
nbr_testcases = int(file.readline())

for test in range(nbr_testcases):
    N, K = tuple([int(k) for k in file.readline().split()])
    if K != 0:
        M = int(math.log(float(K), 2))
        tab = [0 for x in range(M+1)]
        for bit in range(M, -1, -1):
            p = 1 << bit
            if p <= K:
                tab[bit] = 1
                K = K - p
        res = reduce(lambda x,y: x+y, tab[:N])
    else:
        res = 0
    if res == N:
        print "Case #"+str(test+1)+": ON"
    else:
        print "Case #"+str(test+1)+": OFF"

file.close()
