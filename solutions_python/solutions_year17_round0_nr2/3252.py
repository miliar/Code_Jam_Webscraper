#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 18 23:30:41 2017

@author: lin
"""
from __future__ import print_function, division

def is_tidy(x): return x == int(''.join(sorted(str(x))))

T = int(raw_input())  # read a line with a single integer
for case in xrange(1, T + 1):
    num = int(raw_input())
    if is_tidy(num) == True:
        tidy_num = num
    else:
        strnum = [int(digit) for digit in str(num)]
        for i in xrange(len(strnum)-1):
            current = strnum[i]
            nextval = strnum[i+1]
            if current > nextval:
                breakpoint = i
                value = current
                break
            else:
                pass
        for i in xrange(breakpoint, -1, -1):
            if value == strnum[i]:
                breakpoint = i
            else:
                break
        strnum[breakpoint] -= 1
        for i in xrange(breakpoint+1, len(strnum)):
            strnum[i] = 9
        tidy_num = int(''.join([str(x) for x in strnum]))
    print("Case #{0}: {1}".format(case, tidy_num))
