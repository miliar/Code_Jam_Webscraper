#!/usr/bin/python

from __future__ import division
from __future__ import print_function

import itertools
import sys

BLUE = 0
ORANGE = 1

def solve(line):
    line = line.split()
    seq = []
    for i in itertools.count(1, 2):
        try:
            seq.append((int(line[i] == 'O'), int(line[i+1])))
        except IndexError:
            break
    seq = [((i,) + x) for i,x in enumerate(seq)]
    pos = [1, 1] # current positions
    nexts = [None, None] # next step for each robot
    for i, p in enumerate(pos):
        for x in seq:
            if x[1] == i:
                nexts[i] = x
                break
        else:
            nexts[i] = None
    step = 0
    for second in itertools.count(1):
        assert second < 999999
        pushed = False
        for i, p in enumerate(pos):
            n = nexts[i]
            if n is not None:
                if p < n[2]:
                    pos[i] += 1
#                    text = "advance to"
                elif p > n[2]:
                    pos[i] -= 1
#                    text = "retreat to"
                elif step == n[0]:
                    pushed = True
#                    text = "push"
                    for x in seq[step+1:]:
                        if x[1] == i:
                            nexts[i] = x
                            break
                    else:
                        nexts[i] = None
#                else:
#                    text = "stay at"
#            print("Time {0}, robot {1}, {2} {3}".format(second, i, text, pos[i]))
        if pushed:
            step += 1
        if step >= len(seq):
            break
    return second


def main(filename):
    with open(filename, "r") as f:
        for case, line in enumerate(f):
            if not case:
                T = int(line.strip())
                continue
            if case > T:
                break
            print("Case #{0}: {1}".format(case, solve(line)))


if __name__ == "__main__":
    main(sys.argv[1])
    sys.exit(0)

