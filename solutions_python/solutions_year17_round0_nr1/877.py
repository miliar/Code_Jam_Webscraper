# -*- coding: utf-8 -*-
"""
Created on Sat Apr  8 08:41:02 2017

@author: DELL GAMING
"""

t = int(input())
for i in range(1, t + 1):
    s, n = input().split(' ')
    n = int(n)
    a = [1 if x == '+' else -1 for x in s]
    next = 0
    flipp = 0
    for pan in range(len(a)):
        if a[pan] == -1:
            if pan + n > len(a):
                print('Case #{}: IMPOSSIBLE'.format(i))
                next = 1
                break
            else:
                flipp += 1
                for flip in range(pan, pan + n):
                    a[flip] = -a[flip]
    if next == 1:
        continue
    else:
        print('Case #{}: {}'.format(i, flipp))