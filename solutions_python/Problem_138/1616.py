#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
gcm 2014 B
'''

import sys

with open(sys.argv[1]) as f:
    T = int(f.readline())
    for i in range(1, int(T) + 1):
        N = int(f.readline())
        naomi = sorted([float(x) for x in f.readline().split(' ')], reverse=True)
        ken = sorted([float(x) for x in f.readline().split(' ')], reverse=True)

        naomi_copy = naomi[:]
        ken_copy = ken[:]
        naomi_score = 0
        while len(naomi_copy) and len(ken_copy):
            naomi_len = len(naomi_copy)
            ken_len = len(ken_copy)
            if naomi_copy[naomi_len - 1] < ken_copy[ken_len - 1]:
                naomi_copy.pop(naomi_len - 1)
                ken_copy.pop(0)
            else:
                naomi_copy.pop(naomi_len - 1)
                ken_copy.pop(ken_len - 1)
                naomi_score += 1

        naomi_copy = naomi[:]
        ken_copy = ken[:]
        ken_score = 0
        while len(naomi_copy) and len(ken_copy):
            ken_len = len(ken_copy)
            if naomi_copy[0] > ken_copy[0]:
                naomi_copy.pop(0)
                ken_copy.pop(ken_len - 1)
                ken_score += 1
            else:
                naomi_copy.pop(0)
                ken_copy.pop(0)

        print('Case #%d: %d %d' % (i, naomi_score, ken_score))
