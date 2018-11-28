#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
gcm 2014 B
'''

import sys

with open(sys.argv[1]) as f:
    T = int(f.readline())
    for i in range(1, int(T) + 1):
        C, F, X = [float(x) for x in f.readline().split(' ')]
        ans = X / 2
        speed = 2
        farm = 0
        while True:
            speed += F
            farm += 1
            sec = X / speed + sum([C / (2 + x * F) for x in range(0, farm)])
            if sec >= ans:
                break
            else:
                ans = sec
        print('Case #%d: %.7f' % (i, ans))
