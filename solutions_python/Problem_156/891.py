#!/usr/bin/python

import sys

def minTime(P):
#    print P
    maxVal = max(P)
    if max(P) < 4:
        return max(P)

    maxIndex = P.index(maxVal)
    if maxVal == 9:
        P1 = P[:maxIndex] + P[maxIndex+1:] + [5, 4]
        P2 = P[:maxIndex] + P[maxIndex+1:] + [6, 3]
        return min(9, minTime(P1) + 1, minTime(P2) + 1)
    else:
        P1 = [x - 1 for x in P]
        half = maxVal / 2
        P2 = P[:maxIndex] + P[maxIndex+1:] + [half, maxVal - half]
        return min(max(P), minTime(P1) + 1, minTime(P2) + 1)


T = int(sys.stdin.readline())

for t in range(T):
    D = int(sys.stdin.readline())
    P = [int(x) for x in sys.stdin.readline().split()]

    y = minTime(P)

    print "Case #%d: %d" % (t+1, y)
