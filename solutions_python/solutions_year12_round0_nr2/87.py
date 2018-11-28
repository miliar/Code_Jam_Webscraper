#!/usr/bin/python

import os
import sys

fin = sys.stdin

def main():
    T = int(fin.readline())
    for t in xrange(1, T + 1):
        nums = map(int, fin.readline().split())
        N = nums[0]
        S = nums[1]
        p = nums[2]
        nums = nums[3:]
        cutoff_upper = 3 * p - 2    #(p - 1) * 3 + 1
        if cutoff_upper < 0:
            cutoff_upper = 0
        cutoff_lower = 3 * p - 4    #(p - 1) * 3 - 1
        if cutoff_lower < 0:
            cutoff_lower = 0
        count = 0
        for n in nums:
            if n >= cutoff_upper:
                count += 1
                continue
            elif n < cutoff_lower:
                continue
            if S > 0 and n >= 2:
                count += 1
                S -= 1
        print 'Case #%d: %d' % (t, count)

if __name__ == '__main__':
    if len(sys.argv) > 1:
        fin = open(sys.argv[1], 'r')
    main()
