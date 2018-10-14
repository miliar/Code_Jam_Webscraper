#!/usr/bin/env python

import sys

def solve(D, horses):
    times = [(D-K)/float(S) for (K,S) in horses]
    return D / max(times)

if __name__ == "__main__":
    inp = open(sys.argv[1], 'r').readlines()
    T = int(inp[0])
    i = 1
    for t in xrange(T):
        D, N = map(int, inp[i].split())
        i += 1
        horses = []
        for j in range(i, i+N):
            K, S = map(int, inp[j].split())
            horses.append((K, S))
        i += N
        print "Case #%d: %s" % (t+1, solve(D, horses))
