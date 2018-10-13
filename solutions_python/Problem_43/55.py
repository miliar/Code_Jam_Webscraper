#!/usr/bin/python
from __future__ import generators
import sys

def g():
    yield 0
    i = 2
    while True:
        yield i
        i+=1
    

def ReadInts():
    return map(int, sys.stdin.readline().strip().split())

def convert(line, d, base):
    # print line, d, base
    sum = 0
    for x in line:
        sum *= base
        sum += d[x]
    return sum
    
num_cases = ReadInts()[0]
for i in xrange(1, 1+num_cases):
    gen=g()
    line = list(sys.stdin.readline().strip())
    s = set(line)

    if len(line)==1:
        print "Case #%d: %d" % (i,1)
        continue

    # print s
    d = {}
    d[line[0]]=1
    # print "temp",d
    next_i = gen.next()
    for x in line[1:]:
        if x not in d:
            d[x]=next_i
            next_i = gen.next()

    base = len(d)
    if base == 1:
        base = 2

    print "Case #%d: %d" % (i, convert(line, d, base))

