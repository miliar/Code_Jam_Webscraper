#!/usr/bin/env python
# -*- coding: utf-8 -*-
from heapq import *

def read_ints():
    return list(map(int, input().split()))

def solve(t):
    N, r, o, y, g, b, v = read_ints()
    if r == g != 0:
        if o or y or b or v:
            print('Case #{}: IMPOSSIBLE'.format(t))
        else:
            print('Case #{}: {}'.format(t, 'RG'*r))
        return
    if y == v != 0:
        if r or o or g or b:
            print('Case #{}: IMPOSSIBLE'.format(t))
        else:
            print('Case #{}: {}'.format(t, 'VY'*y))
        return
    if b == o != 0:
        if r or y or g or v:
            print('Case #{}: IMPOSSIBLE'.format(t))
        else:
            print('Case #{}: {}'.format(t, 'OB'*b))
        return
    r -= g
    y -= v
    b -= o
    if r < 0 or y < 0 or b < 0:
        print('Case #{}: IMPOSSIBLE'.format(t))
        return
    M = max(r, y, b)
    h = [(-r, r != M, 'R'), (-y, y != M, 'Y'), (-b, b != M, 'B')]
    heapify(h)

    res = ''
    count, _prio, ch = heappop(h)
    while count < 0:
        res += ch
        count, _prio, ch = heapreplace(h, (count + 1, _prio, ch))
    if res[-1] != res[0] and all(count == 0 for count, *_ in h):
        res = res.replace('R', 'RG'*g + 'R', 1)
        res = res.replace('Y', 'YV'*v + 'Y', 1)
        res = res.replace('B', 'BO'*o + 'B', 1)
        print('Case #{}: {}'.format(t, res))
    else:
        print('Case #{}: IMPOSSIBLE'.format(t))

if __name__ == "__main__":
    for t in range(1, int(input())+1):
        solve(t)
