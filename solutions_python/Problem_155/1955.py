#!/usr/bin/python

def doit():
    _, num = raw_input().strip().split()
    ret = 0
    s = 0
    for i, x in enumerate(num):
        x = int(x)
        if i > s:
            ret += i - s
            s = i
        s += x
    return ret

t = input()
for x in xrange(t):
    print 'Case #%d: %d' % (x+1, doit())
