#!/usr/local/bin/python

from sys import stdin

lines = stdin.read().splitlines()
num_cases = int(lines[0])
for case in xrange(num_cases):
    line = lines[case + 1].split(" ")
    s_max = int(line[0])
    count = 0
    sum = 0
    for x in xrange(s_max + 1):
        count += max(x - sum, 0)
        sum += int(line[1][x]) + max(x - sum, 0)

    print "Case #{0}: {1}".format(case + 1, count)
