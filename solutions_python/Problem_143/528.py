# -*- coding: utf-8 -*-
'''
'''
import sys
sys.stdin = open('B-small-attempt0.in')

cases = int(input())
for case_num in range(cases):

    a, b, k = (int(x) for x in input().split())

    count = 0
    for i in range(a):
        for j in range(b):
            if (i & j) < k:
                count += 1

    print('Case #{}: {}'.format(case_num + 1, count))
