# -*- coding: utf-8 -*-

def arrange_day(min):
    if min < 0:
        return min + 24 * 60
    if min > 24 * 60:
        return min - 24 * 60
    return min

def calc(a0, a1):
    p0 = a1[1] - a0[0]
    p1 = a0[1] - a1[0]
    return [arrange_day(p) for p in [p0, p1]]

def solve(AC, AJ, ac, aj):
    if AC + AJ <= 1:
        return 2
    if AC == 1 and AJ == 1:
        return 2

    if AC == 2:
        p = calc(ac[0], ac[1])
    if AJ == 2:
        p = calc(aj[0], aj[1])
    if p[0] <= 12 * 60 or p[1] <= 12 * 60:
        return 2

    return 4

for case in range(1, 1 + int(input())):
    AC, AJ = [int(x) for x in input().split(' ')]
    ac = []
    aj = []
    for l in range(0, AC):
        ac.append([int(x) for x in input().split(' ')])
    for l in range(0, AJ):
        aj.append([int(x) for x in input().split(' ')])

    print('Case #{}: {}'.format(case, solve(AC, AJ, ac, aj)))
