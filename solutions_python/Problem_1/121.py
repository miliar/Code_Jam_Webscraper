#! /usr/bin/env python

import sys

if len(sys.argv) < 3:
    exit()

def check():
    s = set([])
    i = 0
    total = 0
    while i < len(queries):
        while len(s) < len(engines) and i < len(queries):
            s.add(queries[i])
            i += 1
        if len(s) == len(engines):
            s = set([])
            s.add(queries[i-1])
            total += 1
    return total
        
filein = sys.argv[1]
fileout = sys.argv[2]

fin = file(filein)
fout = file(fileout,'w')

N = int(fin.readline())

for i in range(N):
    S = int(fin.readline())
    engines = []
    for s in range(S):
        engines.append(fin.readline().strip())
    Q = int(fin.readline())
    queries = []
    for q in range(Q):
        queries.append(engines.index(fin.readline().strip()))
    m = [];
    for s in range(len(engines)):
        m = check()
    fout.write('Case #%d: %d\n' % ((i+1), m))

fin.close()
fout.close()

