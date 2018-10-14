#!/usr/bin/python

N = int(raw_input())

def solve(pancakes, flipper):
    flips = 0
    for i in range(0, len(pancakes)):
        # print('before', i, flips, pancakes)
        pancake = pancakes[i]
        if pancake == '-':
            # apply flipper
            flips += 1
            for j in range(i, i + flipper):
                if i + flipper > len(pancakes):
                    return "IMPOSSIBLE"
                if pancakes[j] == '-':
                    pancakes[j] = '+'
                else:
                    pancakes[j] = '-'
        # print('after', i, flips, pancakes)
    if '-' not in pancakes:
        return flips
    return "IMPOSSIBLE"


for i in range(0, N):
    pancakes, flipper = raw_input().split(' ')
    flipper = int(flipper)
    pancakes = list(pancakes)
    print("Case #{}: ".format(i+1) +str(solve(pancakes, flipper)))
