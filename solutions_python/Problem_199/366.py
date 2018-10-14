#!/usr/bin/env python

t = int(input())
for i in range(1, t+1):
    pancake, size = input().split(" ")
    size = int(size)
    pancake = [{'+': 0, '-': 1}[ch] for ch in pancake]
    flips = 0
    for j in range(len(pancake)-size+1):
        if pancake[j]:
            flips += 1
            pancake[j:j+size] = [1-i for i in pancake[j:j+size]]

    if set(pancake) == {0}:
        print(f'Case #{i}: {flips}')
    else:
        print(f'Case #{i}: IMPOSSIBLE')

