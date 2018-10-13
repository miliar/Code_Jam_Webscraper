__author__ = 'yushchenko'

import collections
import copy

def f(cnt):
    minc = 1000
    j = sorted(cnt.items())[-1][0]
    if j == 2:
        return 2
    if j == 1:
        return 1
    for i in range(j // 2):
        cnt2 = copy.deepcopy(cnt)
        tmp = cnt2[j]
        cnt2[j - i - 1] += cnt2[j]
        cnt2[i + 1] += cnt2[j]
        del cnt2[j]
        minc = min(minc, f(cnt2) + tmp)

    return min(j, minc)

t = int(input())
for i in range(t):
    n = int(input())
    cnt = collections.Counter()
    for j in input().split():
        cnt[int(j)] += 1

    sum = 0

    print("Case #" + str(i + 1) + ": " + str(f(cnt)))

