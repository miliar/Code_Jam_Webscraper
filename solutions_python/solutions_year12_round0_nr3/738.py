#!/bin/python
import sys

num_tests = int(sys.stdin.readline())

for test in range(num_tests):
    a, b = [int(x) for x in sys.stdin.readline().split()]
    num_digits = len(str(a))
    ans = 0
    for x in range(a, b+1):
        sx = str(x)
        st = set()
        for i in range(1, num_digits):
            if sx[i] != '0':
                y = int(sx[i:] + sx[:i])
                if (y > x) and (y <= b):
                    st.add(y)
        ans = ans + len(st)
    print "Case #%d: %d" % (test + 1, ans)
