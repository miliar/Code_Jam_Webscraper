#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# author: tzeng.yuxio@gmail.com
# usage: ./qround-problem-a.py < sample.in > sample.out

import sys


def get_a_row():
    a = sys.stdin.readline().split()

    return ((int)(a[0]), (int)(a[1]), (int)(a[2]))


def solve():
    x, r, c = get_a_row()

    if (r * c) % x != 0:
        return "RICHARD"
    if min(r, c) * 2 + 1 <= x:
        return "RICHARD"
    if x > max(r, c):
        return "RICHARD"
    if x >= 7:
        return "RICHARD"
    if x >= min(r, c) + 2:
        return "RICHARD"

    return "GABRIEL"

t = (int)(sys.stdin.readline())
for i in range(t):
    print 'Case #' + repr(i + 1) + ': ' + solve()
