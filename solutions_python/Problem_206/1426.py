#!/usr/bin/python

import sys

def NN(): return tuple(map(int, sys.stdin.readline().split()))

T = NN()[0]
for t in range(1, T + 1):
    D, N = NN()
    ks = [NN() for i in range(N)]
    ms = 0
    timePassed = 0.0

    #print ks
    # O(n^2) should be fine !?
    while len(ks) > 1:
        # print timePassed, ks
        ks.sort()
        H = []
        minT = None
        for i in range(len(ks) - 1):
            k1, s1 = ks[i]
            k2, s2 = ks[i+1]
            if s1 > s2:
                T = (k2 - k1) / float(s1-s2)
                #if k1 + T * s1 > D:
                #    T = (D - k1) / s1

                if minT == None or T < minT:
                    minT = T
                    minI = i

        if minT == None:    # time of last horse
            break

        # horse might not catch up before other horse is at the goal.

        # else, let horse catch up.
        ks0 = []
        for i in range(len(ks)):
            k1, s1 = ks[i]
            # ignore caught-up horse
            if i == minI + 1:
                continue

            # ignore horses that made it over the finish line.
            if k1 + minT * s1 > D:
                continue

            if i == minI:
                k2, s2 = ks[i+1]
                assert s1 > s2
                ks0.append((k1 + minT * s1, s2))
            else:
                ks0.append((k1 + minT * s1, s1))

        # all horses made it over the finish line
        if len(ks0) == 0:
            break

        timePassed += minT
        ks = ks0

    k0, s0 = ks[0]
    ms = timePassed + (D - k0) / float(s0)
    #print "total time", ms, ks
    ms = D / ms

    print "Case #%d: %f" % (t, ms)
