#! /usr/bin/env python

import sys

lines = sys.stdin.readlines()

cases = int(lines[0])

for case in xrange(cases):
    C, F, X = map(float, lines[case + 1].split(' '))
    seconds = []
    num_farms = 0
    production = 2.0
    while True:
        seconds_to_win = X / production
        seconds_to_win_with_new_farm = (C / production) + X / (production + F)
        if seconds_to_win < seconds_to_win_with_new_farm:
            seconds.append(seconds_to_win)
            break
        else:
            seconds.append(C/production)
            production = production + F
    total_seconds = sum(seconds)
    print "Case #{0}: {1:.7f}".format(case + 1,  total_seconds)

