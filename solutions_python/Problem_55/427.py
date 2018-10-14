#!/usr/bin/python

import re
import sys


input_file = open('C-small-attempt0.in')
output_file = open('C-small-attempt0.out', 'w')

T = int(input_file.readline())

for t in range(T):
    (R, k, N) = map(int, input_file.readline().split(' '))
    g = map(int, input_file.readline().split(' '))

    euros = 0
    for r in range(R):
        vacant_seats = k
        roller_coaster = []
        while True:
            if len(g) == 0:
                break
            group_size = g[0]
            if vacant_seats < group_size:
                break
            euros += group_size
            roller_coaster.append(group_size)
            vacant_seats -= group_size
            del g[0]
        g.extend(roller_coaster)

    output_file.write("Case #" + str(t + 1) + ": " + str(euros) + "\n")


input_file.close()
output_file.close()
