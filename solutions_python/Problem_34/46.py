#!/usr/bin/python

import sys, re

fin = sys.stdin

line = fin.readline().split()
l = int(line[0])
d = int(line[1])
n = int(line[2])

all = [ fin.readline() for i in range(0, d) ]

for i in range(0, n) :
    pattern = fin.readline().strip().replace("(", "[").replace(")", "]")
    robj = re.compile("^" + pattern + "$")
    ans = 0
    for j in all :
        if (robj.match(j)) : ans = ans + 1
    print "Case #{0}: {1}".format(i + 1, ans)
        
