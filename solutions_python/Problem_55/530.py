#!/usr/bin/env python
import sys

f = open(sys.argv[1])
inputs = int(f.readline())
for input in xrange(1,inputs+1):
    total = 0
    R,k,N = [int(x) for x in f.readline().strip().split()]
    groups = [int(x) for x in f.readline().strip().split()]

    for r in xrange(R):
        car = []
        while len(groups) > 0 and groups[0] + sum(car) <= k:
            total+=groups[0]
            car.append(groups.pop(0))
        groups = groups+car

    print "Case #%d: %d" % (input,total)
