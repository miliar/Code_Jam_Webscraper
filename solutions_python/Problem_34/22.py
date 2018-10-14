#!/usr/bin/python
import sys
import re
rdl = sys.stdin.readline


def process(case):
    """precessing case #"""
    #[int(x) for x in sys.stdin.readline().split()]
    path = rdl().replace('(','[').replace(')',']')
    count = 0
    for w in words:
        if re.match(path, w): count += 1
    return str(count)
    


L, D, cases = rdl().split()
L, D, cases = [int(i) for i in (L, D, cases)]
words = [rdl() for dumb in xrange(D)]
for case in xrange(1, cases+1):
    print "Case #%d:"%case, process(case)
