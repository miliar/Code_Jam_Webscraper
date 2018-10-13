#!/usr/bin/python

# xor

def doit():
    n = input()
    values = map(int, raw_input().strip().split())
    if reduce(lambda x,y: x ^ y, values):
        print 'NO'
    else:
        print sum(values) - min(values)


n = input()
for x in xrange(n):
    print 'Case #%d:' % (x+1),
    doit()
