#! /usr/bin/env python
# -*- coding: utf-8 -*-

from sys import stdin
from fractions import gcd

def gcd2(nums):
    ret = None
    for n in nums:
        if ret == None:
            ret = n
        else:
            ret = gcd(ret, n)
    return ret

count = int(stdin.readline().strip())
for i in range(count):
    nums  = sorted(map(int, stdin.readline().strip().split()[1:]))
    diffs = [nums[j+1] - nums[j] for j in range(len(nums) - 1)]
    T     = gcd2(diffs)
    mod   = nums[0] % T
    if mod == 0:
        result = 0
    else:
        result = T - mod
    print("Case #{0}: {1}".format(i + 1, result))
