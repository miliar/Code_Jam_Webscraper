#!/usr/bin/env python3

from copy import copy

data = open('candy.in')

for i in range(int(data.readline())):
    data.readline()
    candy_str = data.readline().split(' ')
    candies_main = list()
    final = 'NO'
    for cand in candy_str:
        candies_main.append(int(cand))
    for rounds in range(len(candies_main)-1):
        candies = copy(candies_main)
        sean = min(candies)
        candies.remove(sean)
        for iteration in range(rounds):
            next_candy = min(candies)
            candies.remove(next_candy)
            sean ^= next_candy
        patrick = 0
        for remaining in candies:
            patrick ^= remaining
        if sean == patrick:
            final = sum(candies)
            break
        del candies
    print('Case #%d:'%(i+1), final)

