#!/usr/bin/env python

import sys

def time2min(t):
    h, m = map(int, t.split(':'))
    return h * 60 + m

f = open(sys.argv[1])
N = int(f.readline())
for caseno in range(1,N+1):
    T = int(f.readline())

    line = f.readline().split()
    NA = int(line[0])
    NB = int(line[1])

    A = []
    for i in range(NA):
        line = f.readline().split()
        dep = time2min(line[0])
        arr = time2min(line[1])
        A.append((dep,arr))

    B = []
    for i in range(NB):
        line = f.readline().split()
        dep = time2min(line[0])
        arr = time2min(line[1])
        B.append((dep,arr))

    depA = [t[0] for t in A]
    depA.sort()
    rdyA = [t[1]+T for t in B]
    rdyA.sort()
    ntrainA = 0
    for dep in depA:
        # find the closest arrival+T
        oks = [rdy for rdy in rdyA if rdy <= dep]
        if oks == []:
            # no train is ready to go
            ntrainA += 1
        else:
            # ready train is ready no more
            rdyA.remove(max(oks))

    depB = [t[0] for t in B]
    depB.sort()
    rdyB = [t[1]+T for t in A]
    rdyB.sort()
    ntrainB = 0
    for dep in depB:
        # find the closest arrival+T
        oks = [rdy for rdy in rdyB if rdy <= dep]
        if oks == []:
            # no train is ready to go
            ntrainB += 1
        else:
            # ready train is ready no more
            rdyB.remove(max(oks))

            
    print "Case #%d: %d %d" % (caseno, ntrainA, ntrainB)
