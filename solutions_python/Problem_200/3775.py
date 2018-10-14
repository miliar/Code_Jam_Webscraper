#!/usr/bin/python

import sys

lines = int(sys.stdin.readline())

def solve(ds):
    solved = False
    while not solved:
        solved = True
        if ds == '0': break
        ds = ds.lstrip('0')
        for i in range(0, len(ds)-1):
            if ds[i] > ds[i+1]:
                ds = ds[:i] + str(int(ds[i])-1) + '9' * (len(ds) - i - 1)
                solved = False
    return ds

for i in range(1, lines+1):
    line = sys.stdin.readline().strip()
    sol = solve(line)
    print 'Case #%s: %s' % (i, sol)
