#!/usr/bin/env python3

from itertools import tee

def pairwise(iterable):
    a, b = tee(iterable)
    next(b, None)
    return zip(a, b)

t = int(input())
for i in range(1, t + 1):
    print('Case #{}: '.format(i), end='')
    n = [int(c) for c in input()]
    for j, (c1, c2) in enumerate(pairwise(n)):
        if c1 > c2:
            n[j] -= 1
            while j > 0 and n[j] < n[j - 1]:
                j -= 1
                n[j] -= 1
            for k in range(j + 1, len(n)):
                n[k] = 9
            break
    print(int(''.join(map(str, n))))
