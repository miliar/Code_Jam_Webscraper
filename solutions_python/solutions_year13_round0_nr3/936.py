#!/usr/bin/env python

import sys
import math
from itertools import product
import IPython

cumul = [0]
f = open('cumul.dat')
lines = f.read().split('\n')
for line in lines:
    if not line: continue
    x, n = map(int, line.split())
    cumul.append(n)

def count_them(a2, b2):
    return cumul[b2] - cumul[a2-1]


lines = open(sys.argv[1]).read().split('\n')

test_num=int(lines[0])

idx=1
for x in xrange(test_num):
    curr_line = lines[idx]
    idx += 1

    a, b = map(int, curr_line.split(' '))

    # do the search in the sqrt space
    a2 = int(math.ceil(a**.5))
    b2 = int(math.floor(b**.5))

    num = count_them(a2, b2)
    print 'Case #%s: %s' % (x+1, num)
