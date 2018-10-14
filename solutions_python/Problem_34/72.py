#!/usr/bin/python
from sys import stdin
from re import compile
l, d, n = map(int, stdin.readline().split() )
dict = [stdin.readline().strip() for _ in xrange(d)]
c = 1
for line in stdin:
    mo = compile(line.strip().replace("(","[").replace(")","]"))
    print "Case #%d: %d"%(c,sum([ 1 if mo.match(w) else 0 for w in dict ]))
    c += 1
