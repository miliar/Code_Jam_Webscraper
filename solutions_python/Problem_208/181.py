#!/usr/bin/env python
from __future__ import print_function

import sys

INPUT_FILE = "c1.in"
OUTPUT_FILE = "c1.out"

horses = []
dists = []
N = 0

def rec(pos, horse):
    horse = [horse[0], horse[1]]
    next_horse = [horses[pos][0], horses[pos][1]]
    if pos == N-1:
        return 0.0

    dist = dists[pos]
    if horse[0] < dist and next_horse[0] < dist:
        return 1000000000000000000000.0
    elif horse[0] < dist or (horse[1] < next_horse[1] and horse[0] <= next_horse[0]):
        horse = next_horse
        horse[0] -= dist
        return (float(dist) / float(horse[1])) + rec(pos+1, horse)
    elif horses[pos][0] < dist:
        horse[0] -= dist
        return (float(dist) / float(horse[1])) + rec(pos+1, horse)
    else:
        horse[0] -= dist
        res = (float(dist) / float(horse[1])) + rec(pos+1, horse)
        horse = [horses[pos][0], horses[pos][1]]
        horse[0] -= dist
        return min(res, (float(dist) / float(horse[1])) + rec(pos+1, horse))



def log(message):
    print(message, file=sys.stderr)

with open(INPUT_FILE, 'r') as fin, open(OUTPUT_FILE, 'w') as fout:
    sys.stdout = fout

    T = int(fin.readline())
    for tc in range(T):
        log('Test Case %d' % (tc+1))

        N, Q = [int(i) for i in fin.readline().split()]
        horses = []
        dists = []
        for j in range(N):
            E, S = [int(i) for i in fin.readline().split()]
            horses.append((E, S))
        for j in range(N):
            if j == N-1:
                fin.readline()
                break
            dists.append(int(fin.readline().split()[j+1]))

        for j in range(Q):
            U, V = [int(i) for i in fin.readline().split()]

        res = rec(0, [0, 0])

        print('Case #%d: %.6f' % (tc+1, res))
