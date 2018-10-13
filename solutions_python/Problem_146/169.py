#!/usr/bin/env python3
# coding: utf-8

from itertools import permutations

def clean():
    for i, t in enumerate(T):
        r = ' '
        for c in t:
            if r[-1] != c:
                r += c
        T[i] = r[1:]

def solve():
    ans = 0

    oks = set()

    for t in permutations(T):
        seen = {}
        s = ''.join(t)
        p = ''
        ok = True
        if s in oks:
            ans += 1
            continue
        for c in s:
            if c in seen and seen[c] == 0:
                ok = False
                break
            if c not in seen:
                seen[c] = 1
            if c != p:
                seen[p] = 0
            p = c
        if ok:
            oks.add(s)
            ans += 1

    return ans

for case in range(int(input())):
    N = int(input())
    T = list(input().split(' '))
    clean()
    print('Case #{}: {}'.format(case + 1, solve()))
