#!/usr/bin/env python
import sys

def solve(N, M):    
    #print N, M
    tree = {'':{}}
    res = 0
    N.sort()
    M.sort()

    for n in N:
        n = n.split('/')
        size = len(n)
        head = tree
        i = 0
        while i<size:
            if n[i] not in head:
                head[n[i]] = {}
            else:
                head = head[n[i]]
            
            i += 1

    #print tree

    for m in M:
        m = m.split('/')
        size = len(m)
        head = tree
        i = 0
        while i<size:
            if m[i] not in head:
                head[m[i]] = {}
                res += 1
                head = head[m[i]]
            else:
                head = head[m[i]]

            i += 1

    #print tree
    return res

##############################################
newCase = True
Nlines = False
Mlines = False
linesN = []
case = 0

for i,line in enumerate(file(sys.argv[1])):
    line = line.strip()
    if i==0:
        T=int(line)
        continue

    if newCase:
        N,M = map(int,line.split())
        newCase = False
        Nlines = True
        case += 1
        continue

    if len(linesN)<N+M:
        linesN.append(line)
        if len(linesN) == N+M:
            res = solve(linesN[0:N], linesN[N:])
            print "Case #%d: %d" % (case, res)

            linesN = []
            newCase = True
        continue

##############################################

