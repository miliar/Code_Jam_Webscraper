#!/usr/bin/python

def doit():
    n, l, h = map(int, raw_input().strip().split())
    num = map(int, raw_input().strip().split())
    def ok(d):
        for x in num:
            if d % x and x % d: return False
        return True

    for x in xrange(l, h + 1):
        if ok(x):
            print x
            return
    print 'NO'

n = input()
for x in xrange(n):
    print 'Case #%d:' % (x+1),
    doit()
