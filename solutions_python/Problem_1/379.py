#!/usr/bin/env python

import sys

def debug(*s):
    print s

f = open(sys.argv[1])
N = int(f.readline())
for caseno in range(1,N+1):

    S = int(f.readline())
    names = []
    for i in range(S):
        names.append(f.readline().strip())

    Q = int(f.readline())
    queries = []
    for i in range(Q):
        queries.append(f.readline().strip())

    switches = 0
    seen = set()
    for q in queries:
        seen.add(q)
        if len(seen) == S:
            switches += 1
            seen = set([q])
        
    print "Case #%d: %d" % (caseno, switches)
