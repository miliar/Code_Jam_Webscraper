#!/usr/bin/python

import sys

def solve(r, k, n, g):
    if sum(g) < k:
        return r*sum(g)
    cycled = [False] * n
    cycleAt = [0] * n
    curr = 0
    totals = []
    while not cycled[curr]:
        cycled[curr] = True
        total = g[curr]
        i = (curr+1) % n 
        while i != curr and (total + g[i]) <= k:
            total += g[i]
            i = (i+1)%n
        cycleAt[curr] = len(totals)
        totals += [total]
        curr = i
    tail = totals[:cycleAt[curr]]
    cycleRuns = r - len(tail)
    cycle = totals[cycleAt[curr]:]
    cycleGroupLength = len(cycle)
    fullCycles = sum(cycle)*(cycleRuns/(cycleGroupLength))
    finisher = cycle[:(cycleRuns%cycleGroupLength)]
    return sum(tail) + fullCycles + sum(finisher)

def readints(f):
    return [int(s) for s in f.readline().split()]

if __name__ == "__main__":
    f = open(sys.argv[1], "r")
    numCases = int(f.readline())
    for i in xrange(numCases):
        r, k, n = readints(f)
        g = readints(f)
        print "Case #%d: %d" % ((i + 1), solve(r, k, n, g))
    f.close()
