#!/usr/bin/env python
import sys

def solve(c, f, x):
    total_time = 0
    curr_speed = 2

    while True:
        t_wait_goal = x / curr_speed
        t_buy_farm = c / curr_speed
        curr_speed += f

        # Time to goal if we buy farm
        t_goal_get_farm = x / curr_speed

        # If time to new goal + buying the farm is smaller
        # than just waiting, then we want to buy the farm
        if t_goal_get_farm + t_buy_farm < t_wait_goal:
            total_time += t_buy_farm
        else:
            # don't buy farm
            total_time += t_wait_goal
            break

    return total_time

if __name__ == '__main__':
    _f = sys.stdin
    if len(sys.argv) >= 2:
        _f = open(sys.argv[1])

    cases = int(_f.readline())

    for test in xrange(cases):
        c, f, x = [float(v) for v in _f.readline().split()]
        result = solve(c, f, x)

        print "Case #%s: %.7f" % (test + 1, result)

    _f.close()