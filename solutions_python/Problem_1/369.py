#!/usr/bin/env python
import sys

for t in range(int(sys.stdin.readline())):
    engines = {}
    switches = 0
    for e in range(int(sys.stdin.readline())):
        engines[sys.stdin.readline()] = False
    for i in range(int(sys.stdin.readline())):
        q = sys.stdin.readline()
        engines[q] = True
        if not False in engines.values():
            switches += 1
            engines = dict([(k,False) for k in engines.keys()])
            engines[q] = True
    print "Case #%i: %i" %(t+1,switches)
