#!/usr/bin/python

T = int(raw_input())

for l in range(T):
    N = int(raw_input())
    wires = []
    hits = 0
    for i in xrange(N):
        wires.append([int(s) for s in raw_input().split(' ')])
    for i, w1 in enumerate(wires):
        for w2 in wires[i+1:]:
            s1 = w1[0] - w2[0] > 0
            s2 = w1[1] - w2[1] > 0
            if s1 != s2:
                hits += 1
    print "Case #%i: %d" % (l + 1, hits)
