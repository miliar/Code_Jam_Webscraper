#/usr/bin/env python

import sys
import math


DEBUG = False
def debug(string):
    if DEBUG:
        print string


def find_cycle(nums):
    perm = []
    for i in range(1, len(nums)+1):
        if i != nums[i-1]:
            perm.append(i)
            break
    first = perm[0]
    current = perm[0]
    while (True):
        next = nums[current-1]
        perm.append(nums[next-1])
        if next == first:
            break
        current = next
    for i in perm:
        nums[i-1] = i
    return len(perm)-1


in_file = sys.argv[1]
fp = open(in_file)
for case in range (1, int(fp.readline())+1):
    # Init
    debug("Case %s: " % (case))
    nums_count = int(fp.readline())
    string_nums = fp.readline().split()
    nums = []
    for num in string_nums:
        nums.append(int(num))
    debug("%s nums -> %s" % (nums_count, nums))
    count = 0
    # Body
    while (not nums == sorted(nums)):
        changes = find_cycle(nums)
        count += changes
    # Finish
    print "Case #%s: %.6f" % (str(case), count)
    debug("")