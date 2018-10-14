#!/usr/bin/env python

import sys

def solve(n, k):
    # State is the list of sizes of available holes
    state = [n]
    # counts[n] is the number of holes of size n
    counts = {n: 1}

    while k > 0:
        #print state
        #print k, counts

        # Pick the largest hole
        a = state[-1]
        state = state[:-1]
        m = counts.pop(a, None)

        # Should not happen: no hole of this size
        if m == 0:
            continue

        # Compute sizes of the 2 holes created by putting someone
        b = (a-1) / 2
        c = a-1 - b

        #print a, "=", b, "+", c, "+ 1"

        # Split counts[a] holes at the same time
        if m >= k:
            return c, b

        # Add new holes of sizes b and c
        if b not in counts:
            counts[b] = 0
            state.append(b)
        if c not in counts:
            counts[c] = 0
            state.append(c)
        counts[b] += m
        counts[c] += m
        k -= m

        # Keep the state in order
        state = sorted(state)


def solveall(lines):
    count = int(lines[0])
    for i in range(count):
        tmp = lines[i+1].split(' ')
        n = int(tmp[0])
        k = int(tmp[1])
        max, min = solve(n, k)
        print "Case #" + str(i+1) + ":", max, min


if len(sys.argv) != 2:
    sys.stderr.write("Expected one argument (input file)\n")
    exit(1)

lines = []
with open(sys.argv[1], 'r') as ifs:
    for line in ifs:
        lines.append(line.strip())


solveall(lines)

