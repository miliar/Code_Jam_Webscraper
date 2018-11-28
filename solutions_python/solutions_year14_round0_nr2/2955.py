#!/usr/bin/env python

import sys

input = open(sys.argv[1]).readlines()
T = int(input.pop(0).rstrip())

for case in range(1, T+1):
    farm, add_rate, goal = [float(x) for x in input.pop(0).rstrip().split()]
    count = 0.0
    past_time = 0.0
    rate = 2.0
    while count < goal:
        # shall we buy a farm or wait
        rest = goal - count
        if rest < farm:
            # wait
            past_time += rest / rate
            count = goal
        elif rest / rate < farm / rate + rest / (rate + add_rate):
            # wait
            past_time += rest / rate
            count = goal
        else:
            # buy a farm
            past_time += farm / rate
            rate += add_rate
    sys.stdout.write('Case #%s: %s\n' % (case, past_time))
