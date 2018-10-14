#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2013 KuoE0 <kuoe0.tw@gmail.com>
#
# Distributed under terms of the MIT license.

"""

"""

import math


T = int(input())

for t in range(T):

    s, n = [ int(x) for x in raw_input().split() ]

    motes = [ int(x) for x in raw_input().split() ]

    motes.sort()

    if s == 1:
        print "Case #%d: %d" % (t + 1, n)
        continue

    cnt = []
    total = 0
    for i in range(n):

        if s > motes[i]:
            s = s + motes[i]
            cnt.append(total)
        else:
            x = int(math.floor(math.log((motes[i] - 1) / (s - 1), 2))) + 1
            s = 2 ** x * ( s - 1 ) + 1 + motes[i]
            total = total + x
            cnt.append(total)

    ret = n

    for i in range(n):
        ret = min(ret, cnt[i] + (n - i - 1))


    print "Case #%d: %d" % (t + 1, ret)

