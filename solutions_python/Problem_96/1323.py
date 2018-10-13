#!/usr/bin/python
import sys

input = file('B-large.in')
lines = [x.split() for x in input.readlines()]

index = 1
for line in lines[1:]:
    info = map(int, line)
    cases = info[0]
    boost = info[1]
    min = info[2] * 3 - 2
    count = 0
    for case in info[3:]:
        if case >= min:
            count += 1
            continue
        if case >= min - 2 if min - 2 >= 0 else 0:
            if boost > 0:
                boost -= 1
                count += 1

    print "Case #%d: %d" % (index, count)
    index += 1