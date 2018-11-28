from sys import stdin
import re
import operator
import bisect
import sys
import random

def pancakes(p):
    cur_max = p.pop()
    if cur_max <= 3:
        return cur_max
    else:
        if cur_max == 9:
            new_p = p[:]
            bisect.insort(new_p, 3)
            bisect.insort(new_p, 6)
            t9 = pancakes(new_p)
        else:
            t9 = cur_max
        bisect.insort(p, cur_max/2)
        bisect.insort(p, cur_max/2 + cur_max%2)
        return min(cur_max, 1+t9, 1+pancakes(p))

cases = int(stdin.next().strip())
for case in range(1, cases+1):
    D = int(stdin.next().strip())
    p = map(int, stdin.next().split())
    p.sort()
    print 'Case #%d: %d' % (case, pancakes(p))