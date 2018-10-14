#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import collections

fin = sys.stdin
T = int(fin.readline())

for case in range(1, T + 1):
    row1 = int(fin.readline())

    for i in range(4):
        if i == row1-1:
            vals1 = list(map(int,fin.readline().split()))
        else:
            fin.readline()


    row2 = int(fin.readline())

    for i in range(4):
        if i == row2-1:
            vals2 = list(map(int,fin.readline().split()))
        else:
            fin.readline()

    a_multiset = collections.Counter(vals1)
    b_multiset = collections.Counter(vals2)
    overlap = list((a_multiset & b_multiset).elements())


    if len(overlap) == 1:
        print("Case #%d: %d" % (case, overlap[0]))
    elif len(overlap) > 1:
        print("Case #%d: %s" % (case, "Bad magician!"))
    else:
        print("Case #%d: %s" % (case, "Volunteer cheated!"))
