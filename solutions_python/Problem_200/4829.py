#!/usr/bin/env python

t = int(raw_input())

for i in xrange(1, t + 1):
    n = int(raw_input())
    for j in range(n, 0, -1):
        digits = [int(s) for s in str(j)]
        if sorted(digits) == digits:
            print "Case #{}: {}".format(i, "".join(map(str, digits)))
            break
