#!/usr/bin/env python
import sys

def solve(R,k,N,g):
    start = 0
    earnings = 0

    for r in range(R):
        sit = 0
        usedGroups = 0
        while sit <= k and usedGroups<=N:
            sit += g[start % N]
            start += 1
            usedGroups += 1

        start -= 1
        sit -= g[start % N]

        earnings += sit

    return earnings

##############################################

for i,line in enumerate(file(sys.argv[1])):
    line = line.strip()
    if i==0:
        T=int(line)
        continue

    if i%2==1:
        R,k,N = map(int,line.split())
        continue
    else:
        g = map(int,line.split())

        res = solve(R,k,N,g)
        print "Case #%d: %d" % (i/2, res)

##############################################

