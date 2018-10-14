#!/bin/python
#import sys
#sys.stdin = file("sample.in")

def readint(): return int(raw_input())

def readints(): return [ int(x) for x in raw_input().split() ]

def solve(ns):
    from itertools import combinations
    n = len(ns)
    sums = {}
    for x in range(1, n):
        for cm in combinations(ns, x):
            s = sum(cm)
            if sums.has_key(s):
                return [sums[s], cm]
            else:
                sums[s] = cm
    return None

if __name__ == "__main__":
    nt = readint()
    for i in range(nt):
        ns = readints()[1:]
        sols = solve(ns)
        print "Case #%d:" % (i+1)
        if sols is not None:
            for l in sols:
                print " ".join(str(x) for x in l)
        else:
            print "Impossible"
