#!/usr/bin/env python

import os
import sys
from collections import deque

def flip_possibilities(pancakes, k):
    possibilities = []
    for i in xrange(len(pancakes)-k+1):
        possibilities.append(tuple([(not p) if idx >= i and idx < i + k else p
                                    for idx, p in enumerate(pancakes)]))
    return possibilities

def min_flips(pancakes, k):
    cache = set()
    dq = deque([(0, pancakes)])
    while dq:
        cnt, pk = dq.popleft()
        if all(pk):
            return cnt
        cache.add(pk)
        for poss in flip_possibilities(pk, k):
            if poss not in cache:
                dq.append((cnt+1, poss))
    return 'IMPOSSIBLE'

if __name__ == '__main__':
    in_filename = sys.argv[1]
    out_filename = os.path.splitext(in_filename)[0] + '.out'
    with open(in_filename, 'r') as in_f, open(out_filename, 'w') as out_f:
        num_tests = int(in_f.readline())
        for idx, line in enumerate(in_f.readlines()):
            pancakes, k = line.split()
            pancakes = tuple([p == '+' for p in pancakes])
            k = int(k)
            m_flips = min_flips(pancakes, k)
            result = 'Case #{0}: {1}'.format(idx+1, m_flips)
            print result
            out_f.write(result + '\n')