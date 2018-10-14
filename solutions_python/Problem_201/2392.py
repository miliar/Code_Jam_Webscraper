# -*- coding: utf-8 -*-
from itertools import chain

def half(n):
    if n % 2 == 0:
        a = [n / 2 - 1, n / 2]
    else:
        h = (n - 1) / 2
        a = [h, h]
    return [int(x) for x in a]


def listize(e):
    if type(e) == int:
        return [e]
    return e


def solve(x):
    N, K = [int(p) for p in x.split(' ')]
    state = [N]
    for i in range(K):
        max_space = max(state)
        if i == K - 1:
            h = half(max_space)
            return '{} {}'.format(h[1], h[0])
        for j, s in enumerate(state):
            if s == max_space:
                state[j] = half(s)
                state = list(chain.from_iterable(map(listize, state)))
                break

for case in range(1, 1 + int(input())):
    xi = input()
    print('Case #{}: {}'.format(case, solve(xi)))
