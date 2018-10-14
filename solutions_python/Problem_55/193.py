#!/usr/bin/python

import sys

f = open(sys.argv[1])
T = int(f.readline())

for n in range(T):
    arr = f.readline().split()
    trips = int(arr[0])
    size = int(arr[1])
    numgroups = int(arr[2])
    groups = map(int, f.readline().split())
    amt = 0
    for t in range(trips):
        riding = []
        numriding = 0
        while groups != []:
            if numriding + groups[0] > size:
                break
            numriding += groups[0]
            riding.append(groups.pop(0))
        groups.extend(riding)
        amt += numriding
    print "Case #%d: %d" % (n + 1, amt)
