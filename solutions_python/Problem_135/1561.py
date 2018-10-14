#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: d555_
# @Date:   2014-04-12 10:07:47
# @Last Modified by:   d555_
# @Last Modified time: 2014-04-12 10:36:09

import sys
sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w')

T = int(raw_input())

for t in range(1, T + 1):
    fila1 = int(raw_input()) - 1
    M1 = [map(int, raw_input().split()) for i in range(4)]
    fila2 = int(raw_input()) - 1
    M2 = [map(int, raw_input().split()) for i in range(4)]
    inter = list(set(M1[fila1]) & set(M2[fila2]))
    if len(inter) is 1:
        print 'Case #{0}: {1}'.format(t, inter[0])
    elif len(inter) > 0:
        print 'Case #{0}: Bad magician!'.format(t)
    else:
        print 'Case #{0}: Volunteer cheated!'.format(t)
