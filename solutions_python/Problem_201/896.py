# -*- coding: utf-8 -*-
"""
Created on Sat Apr  8 10:07:08 2017

@author: DELL GAMING
"""
from math import log, ceil, floor

t= int(input())
for i in range(1, t + 1):
    n, k = [int(x) for x in input().split(' ')]
    layer = int(log(n, 2))
    live = int(log(k, 2))
    if layer != live:
        acc = 2 ** live
        dis = n - (acc - 1)
        remain = dis % (acc)
        low = floor(dis/acc)
        high = ceil(dis/acc)
        if k - acc + 1 > remain:
            print('Case #{}: {} {}'.format(i, ceil((low-1)/2), floor((low-1)/2)))
        else:
            print('Case #{}: {} {}'.format(i, ceil((high - 1)/2), floor((high - 1)/2)))
    else:
        print('Case #{}: {} {}'.format(i, 0, 0))