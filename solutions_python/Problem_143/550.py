#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2014 jitesh <jitesh@getsuga>
#
# Distributed under terms of the MIT license.

"""

"""

T = int(raw_input())
t = 1
while t <= T:
    a, b, k = map(int, raw_input().split())

    pairs = 0

    for i in xrange(1, a):
        for j in xrange(1, b):
            if (i & j) < k:
                pairs += 1
    pairs += a + b - 1
    print "Case #{0}: {1}".format(t, pairs)
    t += 1
