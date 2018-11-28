#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

with open(sys.argv[1]) as f:
    T = int(f.readline())
    for i in range(1, int(T) + 1):
        ans = set()
        row1 = int(f.readline())
        for j in range(1, 5):
            row = f.readline()
            if row1 == j:
                ans = ans.union([int(x) for x in row.split(' ')])
        row2 = int(f.readline())
        for j in range(1, 5):
            row = f.readline()
            if row2 == j:
                ans = ans.intersection([int(x) for x in row.split(' ')])
        n = len(ans)
        if n == 1:
            print('Case #%d: %d' % (i, list(ans)[0]))
        elif n == 0:
            print('Case #%d: Volunteer cheated!' % i)
        else:
            print('Case #%d: Bad magician!' % i)
