#!/usr/bin/python
# vim: set fileencoding=utf-8 :

import sys

lines = [x.split() for x in sys.stdin.readlines()]

index = 1
for line in lines[1:]:
    robots = {"O": [1, 1], "B": [1, 1]}
    time = 0
    for i in range(int(line[0])):
        r = line[i * 2 + 1]
        d = int(line[i * 2 + 2])
        time = max(time + 1, abs(d - robots[r][0]) + robots[r][1])
        robots[r] = [d, time + 1]
    print "Case #%d: %d" % (index, time)
    index += 1

