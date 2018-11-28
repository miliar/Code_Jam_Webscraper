#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

r_lin = lambda: sys.stdin.readline()
r_int = lambda: int(sys.stdin.readline())
r_flo = lambda: float(sys.stdin.readline())

num_cases = r_int()

for case in xrange(num_cases):
    cookies = 0.0
    seconds = 0.0
    rate = 2.0
    farms = 0.0
    farm_cost, farm_rate, goal = (float(x) for x in r_lin().strip().split())

    def seconds_for_farm(number_of_farms):
        return sum(farm_cost / (rate + n * farm_rate) for n in range(number_of_farms)) + goal / (rate + number_of_farms * farm_rate)

    secs = min(seconds_for_farm(n) for n in range(2500))

    print "Case #{}: {}".format(case + 1, secs)

    

        
