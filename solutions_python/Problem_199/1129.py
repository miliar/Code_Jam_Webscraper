#!/usr/bin/env python

import sys

cases = int(sys.stdin.readline().strip())

for case in range(cases):
    line_v = sys.stdin.readline().strip().split()
    pancakes = [True if x == '+' else False for x in line_v[0]]
    pan_size = int(line_v[1])

    moves = 0
    for pos in range(len(pancakes) - pan_size + 1):
        if not pancakes[pos]:
            moves += 1

            pancakes = pancakes[0:pos] + \
                [not x for x in pancakes[pos:pos+pan_size]] + \
                pancakes[pos+pan_size:]

    sys.stdout.write("Case #%d: " % (case+1))
    if all(pancakes):
        sys.stdout.write("%d\n" % moves)
    else:
        sys.stdout.write("IMPOSSIBLE\n")
