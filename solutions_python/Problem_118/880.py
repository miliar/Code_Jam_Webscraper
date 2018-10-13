#!/usr/bin/python
# -*- coding:utf8 -*-

import sys
from bisect import *


def pal(n):
    return str(n)[::-1] == str(n)

with open(sys.argv[1]) as f:
    plist = [n ** 2 for n in xrange(10 ** 7)
             if pal(n) and pal(n ** 2)]
    T = f.readline().strip()
    for i in xrange(int(T)):
        line = f.readline().strip()
        A, B = line.split(' ')
        ans = bisect_right(plist, int(B)) - bisect_left(plist, int(A))
        print 'Case #' + str(i + 1) + ': ' + str(ans)
