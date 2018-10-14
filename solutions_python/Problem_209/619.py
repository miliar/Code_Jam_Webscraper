# -*- coding: utf-8 -*-
from math import pi
from itertools import combinations as combi

def calc_total_area(side, btm, pattern):
    sides = [side[i] for i in pattern]
    btms = [btm[i] for i in pattern]
    return sum(sides) + max(btms)


def solve(N, K, pcs):
    pcs_side_area = [pc[0] * 2 * pc[1] * pi for pc in pcs]
    pcs_btm_area = [pc[0] * pc[0] * pi for pc in pcs]

    if K == 1:
        ans = max([s + b for (s, b) in zip(pcs_side_area, pcs_btm_area)])
    else:
        patterns = list(combi(list(range(0, N)), K))
        total_area_list = [calc_total_area(pcs_side_area, pcs_btm_area, p) for p in patterns]
        ans = max(total_area_list)

    return str(round(ans, 9))

for case in range(1, 1 + int(input())):
    N, K = [int(x) for x in input().split(' ')]
    pcs = []
    for i in range(1, N + 1):
        pcs.append([int(x) for x  in input().split(' ')])
    print('Case #{}: {}'.format(case, solve(N, K, pcs)))
