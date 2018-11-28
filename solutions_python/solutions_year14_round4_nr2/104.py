#! /usr/bin/python

import os, sys
from collections import OrderedDict

def debug(msg):
    if len(sys.argv) > 1 and sys.argv[1] == '-d':
        sys.stderr.write(msg)
        sys.stderr.write('\n')

T = int(sys.stdin.readline())

def isupdown(l_nums, is_up = True):
    is_already = True
    d = l_nums[0]
    for idx in range(1, len(l_nums)):
        #debug('idx = %s (num=%s, isup=%s)' % (idx, l_nums[idx], is_up))
        if is_up and l_nums[idx] < d:
            is_up = False
        elif not is_up and l_nums[idx] > d:
            is_already = False
            break
        d = l_nums[idx]
    return is_already

def isdown(l_nums):
    return isupdown(l_nums, False)

def changelist_min_begin(l_nums):
    min_elem = l_nums[0]
    idx = 0
    for i in range(1, len(l_nums)):
        if l_nums[i] < min_elem:
            min_elem = l_nums[i]
            idx = i
    return idx, l_nums[0:idx] + l_nums[idx+1:len(l_nums)]

def changelist_min_end(l_nums):
    min_elem = l_nums[0]
    idx = 0
    for i in range(1, len(l_nums)):
        if l_nums[i] < min_elem:
            min_elem = l_nums[i]
            idx = i
    return len(l_nums) - idx - 1, l_nums[0:idx] + l_nums[idx+1:len(l_nums)]

def count(l_nums, res=0):
    if l_nums == []:
        return res
    r1, n1_l_nums = changelist_min_begin(l_nums)
    c1 = count(n1_l_nums, res+r1)
    #
    r2, n2_l_nums = changelist_min_end(l_nums)
    c2 = count(n2_l_nums, res+r2)
    #
    debug('l_nums = %s, c1,r1 = %s,%s, c2,r2 = %s,%s ' % (l_nums, c1, r1, c2, r2))
    return min(c1, c2)

for t in range(1, T+1):
    ret = None
    N = int(sys.stdin.readline())
    nums = [int(x) for x in sys.stdin.readline().split(' ')]
    
    ret = count(nums)
    sys.stdout.write('Case #%s: %s\n' % (t, ret))
        
