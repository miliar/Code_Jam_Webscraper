#!/usr/bin/env python3

import fileinput
from collections import deque

HAPPY = '+'
BLANK = '-'


def solve_min_flips(pancakes, k):
    seen = set()
    queue = deque()
    queue.append((pancakes, 0))

    flip_one = lambda p: {HAPPY: BLANK, BLANK: HAPPY}[p]

    def flip(pancakes, index):
        assert index + k <= len(pancakes)
        return ''.join(flip_one(p) if index <= i < index+k else p for i, p in enumerate(pancakes))

    while len(queue) > 0:
        pancakes, depth = queue.popleft()
        if BLANK not in pancakes:
            return depth
        for i in range(len(pancakes)-k+1):
            proposal = flip(pancakes, i)
            if proposal in seen:
                continue
            seen.add(proposal)
            queue.append((proposal, depth+1))
    
    return 'IMPOSSIBLE'


def main():
    n = int(input())
    for i, line in enumerate(fileinput.input()):
        pancakes, k = line.split()
        flips = solve_min_flips(pancakes, int(k))
        print('Case #{}: {}'.format(i+1, flips))
    assert i == n-1


if __name__ == '__main__':
    main()
