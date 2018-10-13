import sys
from itertools import *
from math import pi
from collections import defaultdict

name = "A-large"
path = ""

sys.stdin = open(path + name + ".in")
sys.stdout = open(path + name + ".out", "w")

T = int(input())

for test_case in range(T):
    N, K = [int(x) for x in input().strip().split()]
    pancakes = []
    for i in range(N):
        pancakes.append([int(x) for x in input().strip().split()] + [i])
    total_sort = sorted(pancakes, key = lambda tup: (tup[0]**2) + (2*tup[0]*tup[1]), reverse=True)
    tup = total_sort[0]
    ans = (tup[0]**2) + (2*tup[0]*tup[1])
    del total_sort[0]
    i = 0
    current_rad = (tup[0]**2)
    while i < K-1:
        best = -1
        best_index = 9999999999
        for j, tup in enumerate(total_sort):
            rad_increase = max(0, (tup[0]**2) - current_rad)
            height_increase = 2*tup[0]*tup[1]
            temp = best
            best = max(best, rad_increase + height_increase)
            if best != temp:
                best_index = j
        ans += best
        current_rad = max(current_rad, total_sort[best_index][0]**2)
        del total_sort[best_index]
        i += 1
    
    print("Case #" + str(test_case + 1) + ": " + str(ans*pi))