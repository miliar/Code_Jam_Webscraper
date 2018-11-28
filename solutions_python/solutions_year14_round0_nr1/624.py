#!/usr/local/bin/python

from sys import stdin

lines = stdin.read().splitlines()
num_cases = int(lines[0])
for case in xrange(num_cases):
    row_1 = lines[case * 10 + 1 + int(lines[case * 10 + 1])].split()
    row_2 = lines[case * 10 + 6 + int(lines[case * 10 + 6])].split()
    matches = list(set(row_1) & set(row_2))
    length = len(matches)
    if length == 1:
        ret = matches[0]
    elif length == 0:
        ret = "Volunteer cheated!"
    else:
        ret = "Bad magician!"
    print "Case #{0}: {1}".format(case + 1, ret)
