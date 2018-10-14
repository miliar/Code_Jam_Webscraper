#!/usr/bin/env python

import sys

cases = int(sys.stdin.readline().strip())

for case in range(cases):
    distance, n_horses = map(int, sys.stdin.readline().split())
    horses = []
    for horse in range(n_horses):
        start, speed = map(int, sys.stdin.readline().split())
        horses.append((start, speed))

    horses.sort()

    opt_time = float("-Inf")
    for start, speed in horses:
        time = float(distance - start)/speed

        if time > opt_time:
            opt_time = time

    sys.stdout.write("Case #%d: %f\n" % (case+1, distance/opt_time))
