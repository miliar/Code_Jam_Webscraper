#!/usr/bin/env python2

import itertools

def do_flips(S, K, x):
    i = 0
    fS = list(S)
    op = {'+':'-', '-':'+'}
    for f in x:
        if f:
            for j in range(K):
                fS[i+j] = op[fS[i+j]]
        i += 1
    return ''.join(fS)

def solve(S, K):
    maxflip = 9999
    happy = "+" * len(S)
    for x in itertools.product([False, True], repeat=(len(S)-K+1)):
        flips = sum(x)
        fS = do_flips(S, K, x)
        if fS == happy:
            maxflip = min(maxflip, flips)
    return "IMPOSSIBLE" if maxflip == 9999 else maxflip

T = int(raw_input())
for i in xrange(T):
    S, sK = raw_input().rstrip().split()
    K = int(sK)
    r = solve(S, K)
    print "Case #%s: %s" % ( (i+1), r )
