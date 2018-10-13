#! /usr/bin/env python
import sys

t = int(sys.stdin.readline())

besttime = {}

def minpos(ls):
    ls.sort(reverse=True)
    mykey = str(ls)
    if mykey in besttime:
        return besttime[mykey]
    if (ls[0] < 3):
        besttime[mykey] = ls[0]
        return ls[0]
    cur = ls[0]
    best = cur
    for i in range(1, ls[0]/2 + 1):
        myls = list(ls)
        myls[0] = i
        myls += [cur-i]
        best = min(best, minpos(myls)+1)
    besttime[mykey] = best
    return best

for i in range(1, t+1):
    d = int(sys.stdin.readline())
    np = []
    for j in sys.stdin.readline().strip().split():
        np += [int(j)]
    print("Case #" + str(i) + ": " + str(minpos(np)))
