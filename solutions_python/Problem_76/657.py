#!/usr/bin/env python

import sys

def runtest(inf, testno):
    best = -1
    N = int(inf.readline())
    line = inf.readline().split()
    candies = map(int, line)
    total = sum(candies)
    for i in xrange(2**N):
        vala = 0
        valb = 0
        val = 0
        for j in xrange(N):
            if i%2 == 1:
                vala = vala^candies[j]
                val += candies[j]
            else:
                valb = valb^candies[j]
            i /= 2
        if vala == valb and vala != 0:
            best = max(val, total-val, best)
    if best < 0:
        print 'Case #' + str(testno+1) + ': NO'
    else:
        print 'Case #' + str(testno+1) + ': ' + str(best)

inf = open(sys.argv[1], 'r')
numtests = int(inf.readline().strip())
for i in xrange(numtests):
    runtest(inf, i)
inf.close()
