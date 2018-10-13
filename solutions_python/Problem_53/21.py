#!/usr/bin/python

def doit():
    n,k = map(int, raw_input().split())
    if (k+1) % 2**n == 0: print 'ON'
    else: print 'OFF'

t=input()
for x in xrange(t):
    print 'Case #%d:' % (x+1),
    doit()
