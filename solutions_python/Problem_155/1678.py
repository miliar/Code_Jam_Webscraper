#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# author: tzeng.yuxio@gmail.com
# usage: ./qround-problem-a.py < sample.in > sample.out

import sys


def get_a_row():
    a = sys.stdin.readline().split()
    b = int(a[0])

    return (b, a[1])


def solve():
    smax, shylvl = get_a_row()
    numInvite = 0
    accu = 0

    for i in range(smax):
        accu += (int)(shylvl[i])
        numInvite = max(numInvite, i + 1 - accu)

    return repr(numInvite)

t = (int)(sys.stdin.readline())
for i in range(t):
    print 'Case #' + repr(i + 1) + ': ' + solve()
