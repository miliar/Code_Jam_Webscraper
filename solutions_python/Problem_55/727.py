#!/usr/bin/env python

import fileinput
from collections import deque

f = fileinput.input()
cases = int(f.readline())
for case in range(1,cases+1):
    (R, k, N) = [int(x) for x in f.readline().split()]
    q = deque([int(x) for x in f.readline().split()])
    sum = 0
    for r in range(R):
        subsum = 0; i = 0
        while q[0] + subsum <= k and i < N:
            subsum += q[0]
            i += 1
            q.rotate(-1)
        sum += subsum
    print("Case #%d: %d" % (case, sum))
