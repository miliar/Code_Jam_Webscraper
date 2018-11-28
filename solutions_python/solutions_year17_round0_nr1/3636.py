#!/usr/bin/env python
# -*- coding: utf-8 -*-

import copy

T = int(input().strip())

for i in range(T):
    s, k = input().split()
    k = int(k)
    cp = copy.copy(s)
    cp = [0 if e == '-' else 1 for e in cp]
    l = len(cp)
    converted = False
    count = 0
    for j in range(l-k+1):
        if cp[j] == 0:
            cp[j:j+k] = [(1 - e) for e in cp[j:j+k]]
            count += 1
    if sum(cp) == l:
        converted = True

    if not converted:
        count = 0
        cp = copy.copy(s)
        cp = [0 if e == '-' else 1 for e in cp]
        for j in range(l-1, k-1, -1):
            if cp[j] == 0:
                cp[j:j-k] = [(1 - e) for e in cp[j:j-k]]
                count += 1
        if sum(cp) == l:
            converted = True

    if converted:
        print('Case #{}: {}'.format(i+1, count))
    else:
        print('Case #{}: {}'.format(i+1, 'IMPOSSIBLE'))
