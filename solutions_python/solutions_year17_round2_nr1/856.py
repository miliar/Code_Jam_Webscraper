#!/usr/bin/env python3

import sys

def print_res(n, res):
    print('Case #{}: {}'.format(n, res))


def solve(dist, horses):
    max_time = 0
    for h in horses:
        to_go = dist - h[0]
        left_time = to_go / h[1]
        if left_time > max_time:
            max_time = left_time
    return dist / max_time

with open(sys.argv[1], 'r') as f:
    test_cases = int(f.readline())
    for tc in range(test_cases):
        line = f.readline().split()
        dist = int(line[0])
        count = int(line[1])
        horses = []
        for i in range(count):
            horse = f.readline().split()
            pos = int(horse[0])
            speed = int(horse[1])
            horses.append((pos, speed))
        res = solve(dist, horses)
        print_res(tc + 1, res)
