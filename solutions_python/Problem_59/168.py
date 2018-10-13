#!/usr/bin/env python

import sys

# find the result
def result(lin, lout):
    nb = 0
    path = {}

    # insert path
    for e in lin:
        full = '/'
        for part in e.split('/'):
            if (part == ''):
                continue
            else:
                full = full + '/' + part
                path[full] = 1

    # count mkdir
    lout.sort()
    for e in lout:
        full = '/'
        for part in e.split('/'):
            if (part == ''):
                continue
            else:
                full = full + '/' + part
                if not path.has_key(full):
                    path[full] = 1
                    nb = nb + 1

    return (nb)

# nb tests
T = int(raw_input())
sys.stderr.write(str(T) + " test to compute\n")

# process tests
for x in xrange(1, T+1):
    sys.stderr.write("[" + str(x) +  "]\tLoad.. ")
    (N, M) = raw_input().split(" ")
    N = int(N)
    M = int(M)

    lin = []
    for y in xrange(N):
        lin.append(raw_input())
    lout = []
    for y in xrange(M):
        lout.append(raw_input())

    sys.stderr.write("Compute.. | ")
    y = result(lin, lout)
    print "Case #" + str(x) + ": " + str(y)
