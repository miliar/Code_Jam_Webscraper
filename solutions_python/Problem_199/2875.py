#!/usr/bin/env python3

import sys

t = int(input())

for i in range(1, t+1):
    pancakes, s = input().split()
    pancakes = list(pancakes)
    s = int(s)
    index = flips = 0
    while index < len(pancakes):
        if pancakes[index] == '-':
            if index >= len(pancakes)-s+1:
                flips = 'IMPOSSIBLE'
                break
            for x in range(index, index + s):
                pancakes[x] = '+' if pancakes[x] == '-' else '-'
            flips += 1
        if pancakes[index] == '+':
            index += 1

    print('Case #{}: {}'.format(i, flips))
