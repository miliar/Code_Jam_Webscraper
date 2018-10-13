#!/usr/bin/env python

import sys
import array
from copy import copy

def can_make_it (speed, pos_init, i, D, T):
    return (pos_init[i] + speed[i]*T >= D)

# find the result
# N = number of chicks
# K = chicks that must be at the end
# D = distance to reach
# T = time
def result(speed, pos_init, N, K, D, T):
    swap = 0
    nb = 0

    pos = copy(pos_init)

    # wait until nb chicks is K
    while 1:
        # pos
        pos[N-1] = pos_init[N-1] + speed[N-1]*T
        for i in range(N-2, -1, -1):
            pos[i] = min(pos[i+1], pos_init[i] + speed[i]*T)

        # nb at the end
        for i in range(N-1, -1, -1): # N-1 to 0
            if pos[i] >= D:
                N = N - 1
                nb = nb + 1

        if nb >= K:
            return swap

        # swap a bad chicken
        swapped = 0

        for i in range(N-1, 0, -1): # N-1 to 1
            # can swap
            if (pos[i] == pos[i-1] and
                can_make_it(speed, pos_init, i-1, D, T)):
                swapped = 1
                swap = swap + 1

                tmp = pos_init[i]
                pos_init[i] = pos_init[i-1]
                pos_init[i-1] = tmp

                tmp = speed[i]
                speed[i] = speed[i-1]
                speed[i-1] = tmp
                break

        # not swapped = impossible
        if swapped == 0:
            return (-1)

# nb tests
C = int(raw_input())
sys.stderr.write(str(C) + " test to compute\n")

# process tests
for x in xrange(1, C+1):
    sys.stderr.write("[" + str(x) +  "]\tLoad.. ")
    (N, K, B, T) = raw_input().split(" ")
    N = int(N)
    K = int(K)
    B = int(B)
    T = int(T)

    pos = [(int(y)) for y in (raw_input().split(' '))]
    speed = [(int(y)) for y in (raw_input().split(' '))]

    pos_a = array.array('l', pos)
    speed_a = array.array('l', speed)

    sys.stderr.write("Compute.. | ")
    y = result(speed_a, pos_a, N, K, B, T)
    if y == -1:
        print "Case #" + str(x) + ": IMPOSSIBLE"
    else:
        print "Case #" + str(x) + ": " + str(y)
