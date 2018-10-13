#! /usr/bin/python

import sys

trial = int(sys.stdin.readline())

for rnd in range(trial):

    A, B, K = [ int(x) for x in sys.stdin.readline().split(' ') ]

    cnt = 0
    for old in range(A):
            for new in range(B):
                if (old & new < K):
                    cnt += 1

    print "Case #%d: %d" % (rnd + 1, cnt)




