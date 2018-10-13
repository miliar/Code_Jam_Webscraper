#!/usr/bin/env python

from sys import argv

def unfeasible(v):
    return reduce(lambda x,y:x^y,v)

def solve(v):
    return "NO" if unfeasible(v) else str(sum(v)-min(v))

f = open(argv[1],'r')
n = int(f.readline())
for x in xrange(n):
    w = int(f.readline())
    v = map(int,f.readline().split())[:w]
    print "Case #%d: %s" % (1+x,solve(v))
