#!/usr/bin/python

import sys

if __name__ == "__main__":
    tests = int(sys.stdin.readline())
    for t in range(tests):
        n = int(sys.stdin.readline())
        all_sum = 0
        all_min = 1000001
        all_xor = 0
        for val in sys.stdin.readline().split():
            val = int(val)
            all_sum += val
            all_min = min(all_min, val)
            all_xor ^= val

        print "Case #%d:" % (t + 1),
        if all_xor == 0:
            print "%d" % (all_sum - all_min)
        else:
            print "NO"
