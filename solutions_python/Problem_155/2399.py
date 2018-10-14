#!/usr/bin/env python2
# -*- coding: utf-8 -*-

from sys import stdin

C = int(stdin.readline())
for c in range(1,C+1):
    sn, s = stdin.readline()[:-1].split()
    sn = int(sn)

    sum = 0
    friends = 0
    for n in range(0, sn + 1):
        if sum < n:
            friends += n - sum
            sum = n
        sum += int(s[n])
    print "Case #%d: %d" % (c, friends)
