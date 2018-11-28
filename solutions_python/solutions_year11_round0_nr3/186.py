#!/usr/bin/python

import sys

def main():
    lines = iter(sys.stdin)
    T = int(next(lines))
    for x in range(1, T+1):
        N = int(next(lines))
        xor = 0
        min_num = float('inf')
        s = 0
        nums = (int(num) for num in next(lines).split())
        for num in nums:
            xor ^= num
            min_num = min(num, min_num)
            s += num
        if xor:
            print "Case #%s: NO" % (x,)
        else:
            print "Case #%s: %s" % (x, s - min_num,)

main()
