#!/usr/bin/env python
from __future__ import division
import sys


INITIAL_COOKIE_RATE = 2


def solve(c, f, x):
    factories = 0
    time = 0

    while True:
        # Calculate the current cookie rate
        cookie_rate = INITIAL_COOKIE_RATE + factories * f

        # Calculate time to buy factory and then end.
        time_to_buy = c / cookie_rate
        time_to_end = x / (cookie_rate + f)
        time_buy_then_end = time_to_buy + time_to_end

        # Calculate time to end at current rate.
        time_to_end_now = x / cookie_rate

        if time_buy_then_end < time_to_end_now:
            # If buying factory is best, buy a factory at first possible time
            #   add time to list, repeat process
            time += time_to_buy
            factories += 1
        else:
            # If waiting is best, do not buy a factory
            #   add time to list, process is finished
            time += time_to_end_now
            break

    return "{0:.7f}".format(time)


if __name__ == '__main__':
    # Read args
    if len(sys.argv) < 2:
        print "USAGE: b.py in_file.in out_file.out"

    with open(sys.argv[1], 'rU') as fin, open(sys.argv[2], 'w') as fout:
        T = int(fin.readline())

        for case in xrange(1, T+1):
            c, f, x = map(float, fin.readline().split())
            soln = solve(c, f, x)

            print >> fout, "Case #{0}: {1}".format(case, soln)
