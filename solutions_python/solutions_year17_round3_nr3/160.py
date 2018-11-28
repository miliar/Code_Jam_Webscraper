#!/usr/bin/env python

for nnn in xrange(1, int(raw_input())+1):
    print "Case #%d:" % (nnn),
    N, K = [int(x) for x in raw_input().split()]
    U = float(raw_input())
    P = [float(x) for x in raw_input().split()]
    P = sorted(P)
    if N!=K:
        continue

    s = 0
    end = N
    for i in xrange(1, len(P)):
        s += P[i-1]
        if i*P[i] - s > U:
            end = i
            break

    if end == N:
        rate = (s+P[-1]+U)/N
        prob = rate**N
    else:
        rate = (s+U)/end
        prob = rate**end
        for i in P[end:]:
            prob *= i
    print prob

