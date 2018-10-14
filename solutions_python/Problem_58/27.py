#!/usr/bin/python

def memo(func):
    cache = {}
    def f(*args):
        if args in cache:
            return cache[args]
        r = func(*args)
        cache[args] = r
        return r
    return f

@memo
def win(a, b):
    if a <= 0 or b <= 0 or a == b: return False
    if a <= b: a, b = b, a
    t = a%b
    while t < a:
        if not win(t, b): return True
        t += b
    return False

def doit():
    a1, a2, b1, b2 = map(int, raw_input().split())
    r = 0
    for a in xrange(a1, a2+1):
        for b in xrange(b1, b2+1):
            if win(a, b):
                r += 1
    return r

t=input()
for x in xrange(t):
    print 'Case #%d: %d' % (x+1, doit())
