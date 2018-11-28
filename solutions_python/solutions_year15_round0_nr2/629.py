#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2015 KuoE0 <kuoe0.tw@gmail.com>
#
# Distributed under terms of the MIT license.

"""

"""
import math

T = input()

for t in range(T):
    D = input()
    Pi = [int(x) for x in raw_input().split(' ')]
    ret = max(Pi)
    # set `cnt` pancake at each disk
    cnt = 2
    while cnt < ret:
        # minus 1 means left at least one pancake at origin disk
        ret = min(ret, sum([(x - 1) // cnt for x in Pi]) + cnt)
        cnt += 1

    print "Case #{0}: {1}".format(t + 1, ret)

