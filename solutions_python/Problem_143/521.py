#!/usr/bin/env pypy
import sys, os

def solving(case, a, b, k):
    wins = 0
    print "\n", case
    for i in range(a):
        for j in range(b):
            if i & j < k:
                wins += 1
    
    outfile.write("Case #%d: %d\n" % (case, wins))

outfile = open("%s.out" % sys.argv[1], "w")
with open(sys.argv[1]) as infile:
    for case, values in enumerate(infile.readlines()[1:]):
        solving(case + 1, *map(int, values.split()))
        
outfile.close()
