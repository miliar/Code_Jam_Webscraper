#!/usr/bin/python
# -*- encoding: utf-8 -*-


def gcd(x, y) :
    while x > 0 and y > 0 :
        if x > y : x %= y
        else : y %= x
    return x + y

T = int(raw_input())
for t in range(1, T + 1) :
    a = raw_input().split()
    n = int(a[0])
    b = [long(x) for x in a[1:]]
    b.sort()

    g = b[1] - b[0]
    for i in range(2, n) :
        g = gcd(g, b[i] - b[i-1])
    k = (b[0] / g) * g - b[0]
    if k < 0 : k += g
    print "Case #%d: %d" % (t, k)
