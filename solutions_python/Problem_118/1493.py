#!/usr/bin/env python

import math
import sys

def filter_palindromes(nums):
    palin_nums = []
    for num in nums:
        numstr = str(num)
        if numstr == numstr[::-1]:
            palin_nums.append(int(num))
    return palin_nums

def parse_intervals(intervalfile):
    num_intervals = int(intervalfile.readline().strip())

    intervals = []
    for line in intervalfile:
        start, end = line.strip().split()
        intervals.append((int(start), int(end)))
    return intervals

if __name__ == '__main__':
    intervals = parse_intervals(open(sys.argv[1]))

    for i, (start, end) in enumerate(intervals, start=1):
        inclusive_roots = range(int(math.floor(math.sqrt(start))), int(math.ceil(math.sqrt(end))) + 1)
        filtered_roots = filter_palindromes(inclusive_roots)
        squares = [x*x for x in filtered_roots]
        squares_in_range = [x for x in squares if x >= start and x <= end]
        num_fair_square = len(filter_palindromes(squares_in_range))
        print 'Case #%d: %d' % (i, num_fair_square)
