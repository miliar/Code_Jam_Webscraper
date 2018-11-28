#!/usr/bin/env python
# vim: set filetype=python et sw=4 ts=4:

import sys
sys.setrecursionlimit(1024*1024)

T = int(sys.stdin.readline())

def seconds_to_reach(target, rate):
    return target/rate

def solve(C, F, X, rate):
    seconds_if_buy = seconds_to_reach(C, rate) + seconds_to_reach(X, rate+F)
    seconds_if_wait = seconds_to_reach(X, rate)
    if (seconds_if_buy < seconds_if_wait):
        seconds = seconds_to_reach(C, rate) + solve(C, F, X, rate+F) 
    else:
        seconds = seconds_if_wait
    return seconds

for case in xrange(T):
    C, F, X = [float(x) for x in sys.stdin.readline().split()]
    sys.stdout.write("Case #%d: %.7f" % (case + 1, solve(C, F, X, 2.0)))
    sys.stdout.write("\n")
