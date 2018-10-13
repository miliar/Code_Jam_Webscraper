#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

input_file = open(sys.argv[1])
if len(sys.argv) > 2:
    ouput_file = open(sys.argv[2], 'w')

def parse(line):
    N, *seq = line.split()
    N = int(N)
    return zip(*[iter(seq)] * 2)


def solve(line):
    seq = parse(line)

    total_sec = 0
    pos = {'O': 1, 'B': 1}
    idle = {'O': 0, 'B': 0}
    the_other = {'O': 'B', 'B': 'O'}
    for who, to in seq:
        to = int(to)
        sec = max(abs(to - pos[who]) - idle[who], 0) + 1
        pos[who] = to
        idle[the_other[who]] += sec
        idle[who] = 0
        total_sec += sec

    return total_sec

cases = int(next(input_file))

for case in range(1, cases + 1):
    print('Case #{case}: {result}'.
          format(case=case, result=solve(next(input_file))),
          file=ouput_file if len(sys.argv) > 2 else sys.stdout, )
