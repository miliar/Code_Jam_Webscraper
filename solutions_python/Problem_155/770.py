#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2015 KuoE0 <kuoe0.tw@gmail.com>
#
# Distributed under terms of the MIT license.

"""

"""

T = input()

for t in range(T):

    tmp = raw_input()
    Smax, X = tmp.split(' ')
    Smax = int(Smax)
    Si = list()
    pSum = [0]

    for c in X:
        Si.append(int(c))
        pSum.append(pSum[-1] + int(c))

    ret = 0
    for i in range(Smax)[::-1]:
        i += 1
        if ret + pSum[i] < i:
            ret += i - (pSum[i] + ret)
    print "Case #{0}: {1}".format(t + 1, ret)



