#!/usr/bin/python

import sys
from itertools import groupby

def solve(seq):
    pos = dict(O=1, B=1)
    prev_robot = 0
    ans = 0
    for robot, grp in groupby(seq, lambda x: x[0]):
        cur = 0
        for i, (robot, button) in enumerate(grp):
            if i == 0:
                cur = max(0, abs(pos[robot] - button) - prev_robot)
                prev_robot = 0
            else:
                cur = abs(pos[robot] - button)
            cur += 1
            ans += cur
            prev_robot += cur
            pos[robot] = button
    return ans

def main():
    lines = iter(sys.stdin)
    T = int(next(lines))
    for lineno, line in enumerate(lines):
        buttons, seq_str = line.split(None, 1)
        seq_raw = seq_str.split()
        seq = list((seq_raw[x*2], int(seq_raw[x*2 + 1])) for x in range(int(buttons)))
        print "Case #%s: %s" % (lineno+1, solve(seq))

main()
