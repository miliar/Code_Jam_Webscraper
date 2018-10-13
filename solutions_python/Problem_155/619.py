from sys import stdin
import re
import operator
import bisect
import sys
import random

cases = int(stdin.next().strip())
for case in range(1, cases+1):
    Smax, audience = stdin.next().split()
    to_add, tot = 0, 0
    for i, v in enumerate(audience):
        if tot < i:
            to_add += i - tot
            tot = i
        tot += int(v)
    print 'Case #%d: %d' % (case, to_add)
