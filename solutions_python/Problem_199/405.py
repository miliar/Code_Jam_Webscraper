#!/usr/bin/env python

import sys

def solve(S, K):
    flips = 0
    S = [1 if s == '+' else -1 for s in S]
    for i in xrange(len(S)):
        if S[i] == -1:
            flips += 1
            if i + K > len(S):
                return "IMPOSSIBLE"
            for j in xrange(i, i+K):
                S[j] *= -1
    assert sum(S) == len(S)
    return str(flips)

if __name__ == "__main__":
    inp = open(sys.argv[1], 'r').readlines()
    T = int(inp[0])
    for t in xrange(T):
        S, K = inp[t+1].split()
        print "Case #%d: %s" % (t+1, solve(S, int(K)))
