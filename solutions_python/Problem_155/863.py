#!/bin/python
import sys

def readFile(fname):
    with open(fname) as f:
            contents = f.read().splitlines()
    ncases = int(contents.pop(0))
    nlines = len(contents)/ncases
    cases = [[] for x in range(ncases)]
    c = 0
    l = 0
    for line in contents:
        cases[c].append(line)
        l += 1
        if l == nlines:
            c += 1
            l = 0
    return cases

def solve(case, c):
    S = case[0].split(' ')[1]
    S = list(map(int, S))
    seen = S.pop(0)
    need = 0
    for i in range(1,len(S)+1):
        if i > seen:
            n = i-seen
            need += n
            seen += n
        seen += S[i-1]
    print("Case #%d: %d" % (c, need))

fname = "test.in"
cases = readFile(fname)
for c in range(len(cases)):
    solve(cases[c], c+1)
