#!/usr/bin/env python3

def flip(pancakes, i, k):
    for j in range(k):
        if pancakes[i + j] == '+':
            pancakes[i + j] = '-'
        else:
            pancakes[i + j] = '+'

def solve(pancakes, k):
    flips = 0
    for i in range(len(pancakes)):
        if pancakes[i] == '+':
            continue
        elif (len(pancakes) - i) < k:
            return 'IMPOSSIBLE'
        else:
            flip(pancakes, i, k)
            flips += 1
    return flips

for i in range(int(input().strip())):
    [pancakes, k] = input().strip().split()
    pancakes = list(pancakes)
    k = int(k)
    print("Case #{}: {}".format(i+1, solve(pancakes, k)))
