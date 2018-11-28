#!/usr/bin/env python3
import math


def add_pancake(bp, idx, R, H):
    if bp[1] is not None and idx not in bp[1]:
        return bp[0] + 2 * R * H + (R ** 2 if bp[0] == 0 else 0)
    else:
        return None

T = int(input())

for t in range(1, T+1):
    N, K = (int(x) for x in input().split())

    backpack = [(0, None) for i in range(K + 1)] 
    backpack[0] = (0, {})


    pancakes = []
    for i in range(N):
        R, H = (int(x) for x in input().split())
        pancakes.append((R, H))

    pancakes.sort()
    pancakes.reverse()

    for (idx, (R, H)) in enumerate(pancakes):
        for i in range(K - 1, -1, -1):
            new = add_pancake(backpack[i], idx, R, H)
            if new is not None and new > backpack[i + 1][0]:
                new_set = set(backpack[i][1])
                new_set.add(idx)
                backpack[i + 1] = (new, new_set)
                
    print("Case #{}: {}".format(t, (backpack[K][0]) * math.pi))
