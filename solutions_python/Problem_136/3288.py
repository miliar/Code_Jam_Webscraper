#!/usr/bin/env python
import sys

line = sys.stdin.readline().strip()
cases = int(line)

for i in range(cases):
    spline = map(float, sys.stdin.readline().strip().split(' '))
    # farm cost
    C = spline[0]
    # farm power
    F = spline[1]
    # goal
    X = spline[2]
    rate = 2.0
    farm = 0
    time = 0.0
    cook = 0.0
    while (True):
        # calculate next time buying farm or goal
        next_farm_delta = (C - cook) / rate
        next_goal_delta = (X - cook) / rate
        next_time = time
        if next_farm_delta < next_goal_delta:
            next_time = time + next_farm_delta
        else:
            #end
            next_time = time + next_goal_delta
            time = next_time
            break
        time = next_time
        #decide to buy a farm or go ahead
        rate_buy = rate + F
        buy_next_goal_delta = (X - cook) / rate_buy
        not_buy_delta = (X - cook - C) / rate
        if (buy_next_goal_delta < not_buy_delta):
            farm += 1
            rate = rate_buy
        else:
            #end
            next_time = time + not_buy_delta
            time = next_time
            break
    sys.stdout.write("Case #%d: %.7f\n" % (i+1, time))


