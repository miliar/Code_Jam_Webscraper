#!/usr/bin/python

def doit():
    def gcd(a, b):
        if b == 0: return a
        return gcd(b, a%b)

    a = map(int, raw_input().split())
    b = []
    for x in a[2:]: b.append(abs(x-a[1]))
    d = b[0]
    for x in b[1:]: d = gcd(d, x)
    k = a[1]%d
    if k == 0: print 0
    else: print d - k


t=input()
for x in xrange(t):
    print 'Case #%d:' % (x+1),
    doit()
