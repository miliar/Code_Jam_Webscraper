#!/bin/python
import sys

num_tests = int(sys.stdin.readline())

for test in range(num_tests):
    data = [int(x) for x in sys.stdin.readline().split()]
    n, s, p = data[:3]
    ans = 0
    for x in sorted(data[3:], reverse=True):
        if (x + 2) / 3 >= p:
            ans = ans + 1
        elif (s > 0) and ((x + 2) / 3 + 1 >= p) and (x > 1):
            ans = ans + 1
            s = s - 1

    print "Case #%d: %d" % (test + 1, ans)
