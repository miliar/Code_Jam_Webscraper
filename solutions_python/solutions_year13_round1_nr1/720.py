#!/usr/bin/env python

import math
import sys

def count_brute(rad, mil):
    current_inner_rad = rad
    rings = 0
    while mil >= 0:
        mil -= 2 * current_inner_rad + 1
        if mil < 0:
            break
        rings += 1
        current_inner_rad += 2
    return rings

def count_equ(rad, mil):
    return math.floor((mil - 2*rad - 1) / 4) + 1

if __name__ == '__main__':
    lines = open(sys.argv[1])
    num_input = int(lines.readline().strip())

    inputs = []
    for line in lines:
        if line.strip():
            inputs.append([int(l.strip()) for l in line.split()])

    for i, (rad, mil) in enumerate(inputs, start=1):
        print "Case #%d: %d" % (i, count_brute(rad, mil))
