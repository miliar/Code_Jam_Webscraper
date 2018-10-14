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

def solve(case_num, reader):
    a, n, vs = read(reader)

    #-----------PROCESS----------
    ans = n;

    pre_sum = a
    pre_ans = 0
    vs = sorted(vs)
    done = 1

    for i, v in enumerate(vs):
        ans = min(ans, pre_ans + n - i)
        while pre_sum <= v and pre_ans < ans:
            pre_sum = 2*pre_sum -1
            pre_ans += 1

        #print i, n, ans, pre_ans, pre_sum, v

        if pre_sum > v:
            pre_sum += v

        else:
            done = 0
            break

    if done:
        ans = min(ans, pre_ans)
    #-----------OUT--------------
    print 'Case #%d: %s' % (case_num, ans)

def main():
    reader = FileWrapper(sys.stdin)
    cases = reader.getInt()
    for i in xrange(cases):
        solve(i+1, reader)

if __name__ == '__main__':
    main()
