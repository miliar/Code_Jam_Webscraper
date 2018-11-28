# -*- coding: utf-8 -*-

import sys
import os
import math

#input_text_path = __file__.replace('.py', '.txt')
#fd = os.open(input_text_path, os.O_RDONLY)
#os.dup2(fd, sys.stdin.fileno())

def flip(A, start_i, K):
    for i in range(start_i, start_i + K):
        if A[i] == '+':
            A[i] = '-'
        else:
            A[i] = '+'

def solve(cakes, K):
    flip_num = 0
    # 左から＋にしていく
    index = 0
    while True:
        #print(cakes)
        if cakes[index] == '+':
            index += 1
        else:
            # ひっくり返す
            flip(cakes, index, K)
            flip_num += 1
            index += 1

        # 終端
        if index > len(cakes) - K:
            break

    if cakes.count('+') == len(cakes):
        return True, flip_num
    else:
        return False, None


f = open('submit.txt', 'w')
N = int(input())
for i in range(N):
    lst = input().split()
    cakes_str = lst[0]
    cakes = list(cakes_str)
    K = int(lst[1])
    #print('Input', cakes_str, K)
    solvable, num = solve(cakes, K)

    if solvable:
        s = 'Case #{}: {}\n'.format(i + 1, num)
        f.write(s)
    else:
        s = 'Case #{}: {}\n'.format(i + 1, 'IMPOSSIBLE')
        f.write(s)

f.close()