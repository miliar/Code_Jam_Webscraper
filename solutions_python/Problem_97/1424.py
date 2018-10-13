#! /usr/bin/python -tt
import itertools
import sys

def perm(num):
    s = list(str(num))
    for i in xrange(1, len(s)):
        pp = s[i:]
        pp.extend(s[:i])
        yield int(''.join(pp))

def check_perm(p, b):
    n = 0
    arr = []
    for i in perm(p):
        if i > p and i <= b:
            arr.append((i, n))
    s = set(arr)
    return len(s)

def recycled(a, b):
    n = 0
    for p in xrange(a, b):
        n = n + check_perm(p, b)
    return n

def ReadInts(f):
    return map(int, f.readline().strip().split())

f = open(sys.argv[1], 'r')
T = ReadInts(f)[0]
for i in xrange(1, T+1):
    a, b = ReadInts(f)
    outp = recycled(a, b)
    print "Case #%d: %s" % (i, outp)
