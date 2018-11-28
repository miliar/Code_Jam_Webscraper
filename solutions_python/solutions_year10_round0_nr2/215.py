#!/usr/bin/env python

def gcd(a, b):
    while a > 0 and b > 0:
        if a > b:
            a = a % b
        else:
            b = b % a

    return a + b


t = raw_input()
for testcase_no in xrange(1, int(t)+1):
    l = [int(x) for x in raw_input().split()]
    n = l[0]
    t = l[1:]
    t.sort()

    g = 0
    for i in xrange(1, len(t)):
        v = t[i] - t[0]
        if g == 0:
            g = v
        else:
            g = gcd(g, v)

    mn = -t[0] + (t[0] / g * g)

    while mn < 0: mn += g

    print "Case #%d: %s" % (testcase_no, mn)

