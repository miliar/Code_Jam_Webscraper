#!/usr/bin/env python

import sys
from math import log, pow, floor, ceil

cases = int(sys.stdin.readline().strip())

for case in range(cases):
    baths, pos = map(int, sys.stdin.readline().strip().split())

    level = int(log(pos)/log(2))
    remaining_toilets_prev_level = baths - (pow(2, level)-1)
    slots, remainder = divmod(remaining_toilets_prev_level, pow(2, level))
    if pos-pow(2,level)+1 <= remainder:
        spare_toilets = slots+1
    else:
        spare_toilets = slots
    partition = (spare_toilets-1)/2.0
    #partition = max(partition, 0)
    left, right = int(ceil(partition)), int(floor(partition))

    sys.stdout.write("Case #%d: %d %d\n" % (
        case+1,
        left,
        right))
