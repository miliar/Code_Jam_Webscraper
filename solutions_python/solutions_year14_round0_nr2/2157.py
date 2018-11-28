#!/usr/bin/python

def get():
    c, f, x = map(float, raw_input().strip().split())
    if c >= x:
        return x / 2.0
    now, cur = 0.0, 2.0
    ret = 0.0
    while now < x:
        if now < c:
            ret += (c - now) / cur
            now = c
        elif (x - now) / cur > c / f:
            now -= c
            cur += f
        else:
            ret += (x - now) / cur
            now = x
    return ret

t = input()
for x in xrange(t):
    print 'Case #%d: %.7f' % (x+1, get())
