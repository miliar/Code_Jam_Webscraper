#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys

f_input = open(sys.argv[1])
problems = int(f_input.readline().rstrip())
for probnum in xrange(1, problems+1):
    mp, counts = f_input.readline().rstrip().split()
    counts = [int(count) for count in counts]

    now = 0
    friends = 0
    for shyness, count in enumerate(counts):
        friends += max(0, shyness-now)
        now += max(0, shyness-now)
        now += count

    print("Case #{}: {}".format(probnum, friends))
