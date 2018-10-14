#!/usr/bin/python

import sys

def comp(S, p, l):
    val = 0
    worst_case = p + 2 * max(p - 2, 0) # Received (p, p - 2, p - 2)

    need_surprise = 0
    for n in l:
        if n < worst_case: # Impossible to achieve the goal value
            continue

        if p * 3 - n <= 2: # Goal value reached without the need of a surprise
            val += 1
            continue

        need_surprise += 1

    return val + min(S, need_surprise)

def solve(fname):
    f = open(fname, 'r')
    f.readline()
    i = 1
    for line in f:
        l = map(int, line.split())

        S = l[1]
        p = l[2]
        l = l[3:]
        print "Case #" + str(i) + ": " + str(comp(S, p, l))
        i += 1
    f.close()

if __name__ == "__main__":
    if len(sys.argv) == 2:
        fname = sys.argv[1]
    else:
        fname = 'B-sample.in'
    solve(fname)
