#!/usr/bin/python

import sys
from sets import Set


def generate_recycled_nums(start, end):
    " Populate recycled_nums "
    recycled_nums = { }

    for num in range(start, end+1):
        s = str(num)
        
        if s in recycled_nums:
            continue

        # Set containing a number and its recycles
        recycled_num_set = set()
        recycled_nums[s] = recycled_num_set

        # Recycle a number
        for i,ch in enumerate(s):
            res = s[i:] + s[:i]
            res = int(res)
            res = str(res)
            if len(res) != len(s):
                continue
            recycled_nums[res] = recycled_num_set
            recycled_num_set.add(res)

    return recycled_nums

def count_recycled_nums_between(start, end, recycled_nums):
    " Inclusive "
    count = 0
    for num in range(start, end + 1): # inclusive
        s = str(num)

        if not s in recycled_nums:
            continue

        if len(recycled_nums[s]) <= 1:
            continue

        num_set = recycled_nums[s]
        for candidate in num_set:
            if s == candidate: # Overcounting
                continue
            if candidate < s: # More overcounting
                continue

            if start <= int(candidate) <= end:
                count += 1

    return count

if __name__ == "__main__":
    recycled_nums = generate_recycled_nums(0, 2000000)
    num_lines = int(sys.stdin.readline())
    count = 1
    for line in sys.stdin.readlines():
        if line.strip() == '':
            continue
        splitline = line.split(' ')
        start, end = int(splitline[0]), int(splitline[1])
        print "Case #%d: %d" % (count, count_recycled_nums_between(start, end, recycled_nums))
        count += 1

