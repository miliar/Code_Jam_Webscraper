#!/usr/bin/python3

from itertools import product

T = int(input())

for t in range(T):
    N, M = list(map(int, input().split()))
    grid = [list(map(int, input().split())) for n in range(N)]
    rowmax = list(map(max, grid))
    colmax = list(map(max, map(list, zip(*grid))))
    for n, m in product(range(N), range(M)):
        #print(n, m, grid[n][m])
        if grid[n][m] != rowmax[n] and grid[n][m] != colmax[m]:
            print("Case #{}: NO".format(t + 1))
            break
    else:
        print("Case #{}: YES".format(t + 1))
