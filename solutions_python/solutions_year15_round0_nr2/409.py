#!/usr/bin/env python
import fileinput
f = fileinput.input()
T = int(f.readline())
for t in range(T):
    d = int(f.readline())
    P = f.readline().strip().split()
    P = map(int, list(P))
    P.sort()
    maxP = max(P)
    # print P, "dash", d, "max p", maxP
    H = [0] * 1001
    for p in P: # count
        H[p] += 1
    for i in range(maxP-1, 0, -1): # acc count
        H[i] += H[i+1]
    # print H[1:maxP+1]
    time = [0] * (maxP+1)
    # Brute force searching for best pancake cut size
    for mincut in range(1, maxP+1, 1):
        # cut at every multiple of best pancake cut size
        cutat = range(mincut+1, maxP+1, mincut)
        cuts = map(lambda x:H[x], cutat)
        #print cuts, "cut every", mincut, "time", sum(cuts) + mincut
        time[mincut] = sum(cuts) + mincut
    mintime = min(time[1:])
    #print "min", mintime
    print 'Case #{}: {}'.format(t+1, mintime)
