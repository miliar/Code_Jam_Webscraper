#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vi:ts=4 sw=4 et

from __future__ import division

import sys



def run_testcase():
    N = int(raw_input().strip())
    candies = [int(x) for x in raw_input().strip().split()]

    xor = reduce(lambda x,y: x ^ y, candies)
    total = sum(candies)
    answer = total - min(candies)

    if xor:
        return "NO"
    else:
        return str(answer)


max_testcases = int(raw_input().strip())
for T in range(1, max_testcases+1):
    print "Case #{0}: {1}".format(T, run_testcase())
