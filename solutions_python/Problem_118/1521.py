#!/usr/bin/env python

# Say
#   ./c.py 10000000
# to prepare the array of counts used by the solver.
#
# Say
#   ./c.py < C.in > C.out
# to solve input C.in.

import sys
import bisect


def read_int():
    return int(raw_input())

def read_ints():
    return map(int, raw_input().split())

def palindromep(n):
    s = str(n)
    return s == s[::-1]

nums = [1, 4, 9, 121, 484, 10201, 12321, 14641, 40804, 44944, 1002001, 1234321, 4008004, 100020001, 102030201, 104060401, 121242121, 123454321, 125686521, 400080004, 404090404, 10000200001, 10221412201, 12102420121, 12345654321, 40000800004, 1000002000001, 1002003002001, 1004006004001, 1020304030201, 1022325232201, 1024348434201, 1210024200121, 1212225222121, 1214428244121, 1232346432321, 1234567654321, 4000008000004, 4004009004004] 

def precompute(end):
    nums = []
    for n in xrange(1, end + 1):
        if palindromep(n):
            square = n * n
            if palindromep(square):
                nums.append(square)
    print nums

def solve():
    t = read_int()
    for caseno in xrange(1, t+1):
        a, b = read_ints()
        aidx = bisect.bisect_left(nums, a)
        bidx = bisect.bisect_left(nums, b)
        if bidx < len(nums) and nums[bidx] == b:
            bidx += 1
        print "Case #%d: %d" % (caseno, bidx-aidx)


if len(sys.argv) > 1:
    precompute(int(sys.argv[1]))
else:
    solve()
