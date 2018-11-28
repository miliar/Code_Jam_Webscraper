#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: d555_
# @Date:   2014-04-12 10:38:14
# @Last Modified by:   d555_
# @Last Modified time: 2014-04-12 15:10:53
import sys
sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w')


T = int(raw_input())

for t in range(1, T + 1):
    C, F, X = map(float, raw_input().split())
    total = 0
    if X <= C:
        total = X / 2
    else:
        f = 2
        while True:
            if C / f + X / (f + F) > X / f:
                total += X / f
                break
            else:
                total += C / f
                f += F

    print 'Case #%d:' % t,
    print '%0.7f' % total
