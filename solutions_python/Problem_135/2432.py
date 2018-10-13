#! /usr/bin/env python

import sys

lines = sys.stdin.readlines()

cases = int(lines[0])

for case in range(cases):
    row_num = int(lines[case * 10 + 1])
    second_row_num = int(lines[case * 10 + 6])
    row = lines[case * 10 + 1 + row_num]
    second_row = lines[case * 10 + 6 + second_row_num]
    row = map(int, row.split(' '))
    second_row = map(int, second_row.split(' '))
    common = set(row) & set(second_row)
    if len(common) < 1:
        print "Case #{0}: Volunteer cheated!".format(case + 1)
    elif len(common) > 1:
        print "Case #{0}: Bad Magician!".format(case + 1)
    else:
        print "Case #{0}: {1}".format(case + 1, common.pop())
