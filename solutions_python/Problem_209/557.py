#!/usr/bin/env python3
import fileinput
import math

inp = fileinput.input()

T = int(inp.readline())
def side_surface(tup):
    return 2.0 * math.pi * tup[0] * tup[1]
def top_surface(tup):
    return math.pi * tup[0] * tup[0]

for t in range(1, T+1):
    N, K = [int(x) for x in inp.readline().split()]
    pancakes = []
    for n in range(N):
        R, H = [int(x) for x in inp.readline().split()]
        pancakes += [(R, H, side_surface((R, H)), top_surface((R, H)),
                      side_surface((R, H)) + top_surface((R, H)))]
    sorted_by_side = sorted(pancakes, key=lambda tup: tup[2],reverse=True)
    sum = 0.0
    for i in range(K - 1):
        sum += sorted_by_side[i][2]
    biggest_sum = 0.0
    for i in range(K - 1, N):
        biggest_top_surface = sorted(sorted_by_side[:(K-1)] + [sorted_by_side[i]],
                                     key=lambda tup: tup[3],reverse=True)[0]
        tmp = sum + sorted_by_side[i][2] + biggest_top_surface[3]
        if tmp > biggest_sum:
            biggest_sum = tmp
    print("Case #{}: {}".format(t, biggest_sum))


