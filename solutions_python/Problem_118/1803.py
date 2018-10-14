#!/usr/bin/env python
from math import *


mem = []


def pal(n):
        n = str(n)
        return n == n[::-1]


def fill(n):
    t = int(ceil(sqrt(n)))
    for i in range(t+1):
        ii = i*i
        if pal(i) and pal(ii) and ii <= n:
            mem.append(ii)


def fair_and_square(a, b):
    c = 0
    for num in mem:
        if a <= num:
            if num > b:
                return c
            c += 1
    return c

fill(10**14)

import sys
data = open(sys.argv[1], 'r').read()
data = data.split('\n')
data.reverse()
T = int(data.pop())

for i in xrange(T):
    a, b = map(int, data.pop().split())
    print 'Case #%s: %s' % (i+1, fair_and_square(a, b))
