#! /usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import math

def isPalindrome(d):
    int_str = str(d)
    rev_str = int_str[::-1]
    if (int_str == rev_str):
        return True
    else:
        return False

T =  int(sys.stdin.readline())

for x in range(T):
    tmp = list(map(int, sys.stdin.readline().split()))
    minimum = tmp[0]
    maximum = tmp[1]
    rt_min = int(math.sqrt(minimum))
    rt_max = int(math.sqrt(maximum)) + 1

    count = 0
    for d in range(rt_min, rt_max+1):
        if (d * d >= minimum and d * d <= maximum and
            isPalindrome(d * d) and isPalindrome(d)):
            count += 1

    print("Case #%d: %d" % (x+1, count))
