# -*- coding: utf-8 -*-

import sys
import os
import math
from decimal import Decimal
import itertools

input_text_path = __file__.replace('.py', '.txt')
fd = os.open(input_text_path, os.O_RDONLY)
os.dup2(fd, sys.stdin.fileno())

T = int(input())

f = open('submit.txt', 'w')
for t in range(T):
    print()
    print('テスト', t)
    N, K = map(int, input().split())
    pancakes = []
    for i in range(N):
        R, H = map(int, input().split())
        circle = Decimal(R) * Decimal(R) * Decimal(math.pi)
        side = Decimal(2) * Decimal(math.pi) * Decimal(R) * Decimal(H)
        area = circle + side
        pancakes.append((R, H, side, circle, area))

    area_list = []
    # select by combination
    for selected_pancakes in itertools.combinations(pancakes, K):
        selected_pancakes = list(selected_pancakes)
        print(selected_pancakes)
        area_sum = 0
        selected_pancakes.sort() # sort by R
        area_sum += selected_pancakes[0][-1]
        circle = selected_pancakes[0][-2]

        for i in range(1, K):
            cake = selected_pancakes[i]
            area_sum += cake[-1] # area
            area_sum -= circle
            circle = cake[-2]
        area_list.append(area_sum)

    S = max(area_list)



    answer = 'Case #{}: {:.9f}'.format(t+1, S)
    print(answer)
    f.write(answer)
    if t != T-1:
        f.write('\n')
f.close()
