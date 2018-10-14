#!/usr/bin/python
import os, sys
from math import *

exercise = os.path.split(__file__)[1][0] # A,B,C...
if len(sys.argv) > 1:
    variant = sys.argv[1] # sample, small-attempt0, ...
else:
    variant = raw_input('input variant: ')
input = '%s-%s.in' % (exercise,variant)
print 'reading input', input
input = file(input)
output = '%s-%s.out' % (exercise,variant)
print 'writing output', output
output = file(output,'w')

T = int(input.readline())


def fac(n):
    """http://rosettacode.org/wiki/Prime_decomposition#Python"""
    step = lambda x: 1 + x*4 - (x//2)*2
    maxq = long(floor(sqrt(n)))
    d = 1
    q = n % 2 == 0 and 2 or 3
    while q <= maxq and n % q != 0:
        q = step(d)
        d += 1
    res = []
    if q <= maxq:
        res.extend(fac(n//q))
        res.extend(fac(q))
    else: res=[n]
    return res

assert set(fac(12)) == set([2,2,3])

def solve():
    N, D = map(int,input.readline().split('/'))
    print '%s/%s' % (N,D)
    fs = fac(D)
    for f in fs:
        if f==2:
            continue
        assert D % f == 0
        if True:
            if N % f != 0:
                return 'impossible'
            N = N//f
            D = D//f
            print 'reduced by %s: %s/%s' % (f,N,D)
    p = D.bit_length() - 1
    assert 2**p == D
    for n in range(41):
        if N * 2**n >= 2**p:
            return n
    print 'more than 40 ancestors for %s/%s' % (N,D)
    return 'impossible'


for t in range(T):
    print >> output, 'Case #%s: %s' % (t+1,solve())
