from collections import deque, Counter
import heapq
import math

def comp(l, i, j):
    if i == -1:
        return True
    mini = min(l[i])
    minj = min(l[j])
    if mini == minj:
        maxi = max(l[i])
        maxj = max(l[j])
        return maxj > maxi
    return minj > mini

def update(stalls, i):
    minj = i - 1
    maxj = i + 1
    while minj >= 0 and stalls[minj] is not False:
        stalls[minj] = (stalls[minj][0], i - minj - 1)
        minj -= 1
    while maxj < len(stalls) and stalls[maxj] is not False:
        stalls[maxj] = (maxj - i - 1, stalls[maxj][1])
        maxj += 1


def solve(line):
    n, k = map(int, line.split())
    if n == k:
        return "0 0"
    stalls = [(i, n-(i+1)) for i in range(n)]
    last = ()
    for i in range(k):
        maxi = -1
        for j in range(n):
            if stalls[j] and comp(stalls, maxi, j):
                maxi = j
        last = stalls[maxi]
        stalls[maxi] = False
        # print(stalls)
        update(stalls, maxi)
        # print(stalls)
    # print(maxi)
    # print(last)
    return " ".join(map(str, sorted(last, reverse=True)))

import functools

@functools.lru_cache()
def cumalative(n):
    total = 0
    for i in range(n):
        total += 2**i
    return total

def solve2(line):
    n, k = map(int, line.split())
    if n == k:
        return "0 0"
    stalls = [(i, n-(i+1)) for i in range(n)]
    l = math.log(k, 2)
    dec, intg = math.modf(l)
    factor = int(intg) + 1
    loc = math.ceil(dec * 2**intg)
    loc =  (loc if loc else loc + 1)
    # print(loc)
    # b1 = 2 ** factor
    # lower = cumalative(factor-1)
    # upper = cumalative(factor)
    l, m, u = 0, n//2, n
    separation = n / 2**factor
    rough_estimate = separation * loc
    # print(rough_estimate)
    for i in range(factor-1):
        mid1 = l + (m-l)//2
        mid2 = m + (u-m)//2
        new_left_l = l
        new_left_m = mid1
        new_left_u = m
        new_right_l = m + 1
        new_right_m = mid2
        new_right_u = u
        if rough_estimate < m:
            l, m, u = new_left_l, new_left_m, new_left_u
        else:
            l, m, u = new_right_l, new_right_m, new_right_u
    # print(l, m, u)
    last = (m-l, u-m-1)
    return " ".join(map(str, sorted(last, reverse=True)))



num = int(input())
for i in range(1, num+1):
    line = input()
    print("Case #{}: {}".format(i, solve(line), solve2(line)))
