# -*- coding: utf-8 -*-

import re
import sys
import os
import time
import itertools
import collections
import logging

sys.path.insert(0, "..")

from base import *

logger = config_logger()

def read(reader):
    a, n = reader.getInts()
    vs = reader.getInts()
    return a, n, vs

def sum_diff(start, k, step):
    return k * (start + start + step * (k-1)) / 2;

def ok(s):
    for x in s:
        if x not in 'aeiou':
            return 0
    return 1

def solve(case_num, reader):
    name, n = reader.getWords()[:2]
    n = int(n)
    #-----------PROCESS----------
    ans = 0;
    segs = []

    i = 0
    m = len(name)
    while i < m:
        if name[i] in 'aeiou':
            i+=1
            continue
        j = i
        while j < m and name[j] not in 'aeiou':
            j = j + 1

        if j - i >= n:
            for a in range(i, j):
                for b in xrange(a+n-1, j):
                    segs.append((a,b))

        i = j + 1

    for a in xrange(m):
        for b in xrange(a+n-1, m):
            for x, y in segs:
                if a<=x and b>=y:
                    ans+=1
                    break


    #-----------OUT--------------
    print 'Case #%d: %s' % (case_num, ans)

def main():
    reader = FileWrapper(sys.stdin)
    cases = reader.getInt()
    for i in xrange(cases):
        solve(i+1, reader)

if __name__ == '__main__':
    main()
