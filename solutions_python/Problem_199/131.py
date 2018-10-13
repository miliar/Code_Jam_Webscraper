#!/usr/bin/env python3

from functools import reduce
from operator import and_

T = int(input().strip())

for t in range(T):
    print("Case #{}: ".format(t + 1), end="")
    
    pancakes, flipper = input().strip().split(" ")
    flipper = int(flipper)
    pancakes = [pancake == "+" for pancake in pancakes]
    
    flips = 0
    for i in range(len(pancakes) - flipper + 1):
        if not pancakes[i]:
            for j in range(i, i+flipper):
                pancakes[j] ^= True
            flips += 1
    if reduce(and_, pancakes[-flipper:], True):
        print(flips)
    else:
        print("IMPOSSIBLE")

