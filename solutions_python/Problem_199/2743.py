#!/usr/bin/env python

import fileinput
import sys
import time

TIME_LIMIT_S = 3*60
# TIME_LIMIT_S = 5

def bfs_solve(state, K, L, S, until):
    states = [(0, state)]
    checked = [state]

    while len(states) > 0 and time.time() < until:
        # Get state
        steps, state = states.pop(0)

        # Check if done
        if sum(state) == L:
            return steps

        # Get next states
        for i in range(0, S):
            nextstate = list(state)
            nextstate[i:i+K] = [e * -1 for e in nextstate[i:i+K]]
            if nextstate not in checked:
                states.append((steps + 1, nextstate))
                checked.append(nextstate)

    return -1

if __name__ == "__main__":
    case = 0
    start = time.time()
    stop = start + TIME_LIMIT_S

    for line in fileinput.input():
        line = line.rstrip()

        if case == 0:
            T = int(line)
        else:

            split = line.split(" ")

            state = [44 - ord(c) for c in split[0]]

            K = int(split[1])

            L = len(state)
            S = L - K + 1

            until = stop
            if case < T:
                until = time.time() + (stop - time.time()) / (T - case)

            print(line, file=sys.stderr)

            steps = bfs_solve(state, K, L, S, until)

            if steps < 0:
                steps = "IMPOSSIBLE"

            print("\tCase #%d: %s" % (case, steps), file=sys.stderr)
            print("Case #%d: %s" % (case, steps))

        case += 1
