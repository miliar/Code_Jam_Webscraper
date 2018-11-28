#!/usr/bin/python

import sys

def solve(L, H, others):
    pos = range(L, H+1)
    for o in others:
        offset = 0
        for p in range(len(pos)):
            pcor = p-offset

            if pos[pcor] % o != 0 and \
               o % pos[pcor] != 0:
               del pos[pcor]
               offset += 1
    if not pos:
        return "NO"
    return pos[0]

T = int(sys.stdin.readline())

for t in range(T):
    line = sys.stdin.readline()
    N, L, H = [int(x) for x in line.split()]
    line = sys.stdin.readline()
    others = [int(x) for x in line.split()]
    sol = solve(L, H, others)
    print "Case #" + str(t+1) + ": " + str(sol) 
