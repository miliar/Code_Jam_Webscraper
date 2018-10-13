# -*- coding: utf-8 -*-

fin = open("a.in","r")
T = int(fin.readline())

for i in range(1,T+1):
    N = int(fin.readline())
    lengths = []
    for j in range(N):
        line = fin.readline()
        l = 0
        for s, c in enumerate(line):
            if c == '1':
                l = s+1
        lengths.append(l)
    swaps = 0
    for j in range(N):
        for k in range(N-j):
            if lengths[k] <= j+1:
                break
        del lengths[k]
        swaps += k
    print "Case #%d: %d" % (i, swaps)