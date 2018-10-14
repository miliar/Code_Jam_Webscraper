from __future__ import print_function
import sys
import math
from collections import deque

f = sys.stdin

if len(sys.argv) > 1:
    f = open(sys.argv[1], "rt")


T = int(f.readline().strip())

for case_id in range(1, T+1):
    N = int(f.readline().strip())
    Na_stones = sorted(map(float, f.readline().strip().split()))
    Ke_stones = sorted(map(float, f.readline().strip().split()))
    #~ print(N)
    #~ print(Na)
    #~ print(Ke)

    ken_points = 0
    i = 0
    for na_value in Na_stones:
        while i < N and Ke_stones[i] < na_value:
            i += 1
        if i < N:
            ken_points += 1
            i += 1

    na_cheat_points = 0
    na_left_stones = deque(Na_stones)
    ke_left_stones = deque(Ke_stones)

    while len(na_left_stones) > 0:
        #~ print(na_left_stones)
        #~ print(ke_left_stones)
        if na_left_stones[0] > ke_left_stones[-1]:
            na_cheat_points += len(na_left_stones)
            break
        if ke_left_stones[0] > na_left_stones[-1]:
            break
        if na_left_stones[0] > ke_left_stones[0]:
            na_left_stones.popleft()
            ke_left_stones.popleft()
            na_cheat_points += 1
        else:
            na_left_stones.popleft()
            ke_left_stones.pop()

    resCheat = na_cheat_points
    resFair = N - ken_points
    print(str.format('Case #{0}: {1} {2}', case_id, resCheat, resFair))
