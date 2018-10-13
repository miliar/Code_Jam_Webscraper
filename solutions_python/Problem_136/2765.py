#/usr/bin/env python2
# -*- coding: utf-8 -*-

import sys
from pprint import pprint

nb_tests = int(sys.stdin.readline())

for test in range(nb_tests):
    C, F, X = [float(data) for data in sys.stdin.readline().split(' ')]

    time = 0.0
    cookies = 0.0
    cookies_per_sec = 2.0
    while cookies != X:
        time_for_farm = time + (C / cookies_per_sec)
        time_for_goal = time + (X / cookies_per_sec)
        next_time_for_farm = time_for_farm + ( C / (cookies_per_sec + F) )
        next_time_for_goal = time_for_farm + ( X / (cookies_per_sec + F) )
        
        if time_for_goal < next_time_for_farm or time_for_goal < next_time_for_goal:
            cookies = X
            time = time_for_goal
        else:
            cookies_per_sec += F
            cookies = 0 # not necessary
            time = time_for_farm

    print "Case #%s: %.7f" % (test + 1, time)

