from __future__ import division

import sys
from decimal import Decimal

BASE_RATE = 2

def best_time(farm_cost, farm_bonus, cookie_goal):
    # Assume a (kinda) greedy strategy
    strategy_found = False
    time_spent = 0
    current_rate = BASE_RATE

    while not strategy_found:
        time_to_farm = farm_cost / current_rate
        better_rate = current_rate + farm_bonus

        if cookie_goal / current_rate < time_to_farm + cookie_goal / better_rate:
            # Just waiting for cookies is the best we can now do
            strategy_found = True
            time_spent += cookie_goal / current_rate
        else:
            time_spent += time_to_farm
            current_rate = better_rate

    return time_spent

if __name__ == "__main__":
    num_cases = int(sys.stdin.readline().strip())
    for c_n in xrange(num_cases):
        farm_cost, farm_bonus, cookie_goal = map(float, sys.stdin.readline().strip().split())
        time = best_time(farm_cost, farm_bonus, cookie_goal)
        print "Case #%d: %0.7f" % (c_n + 1, time)
