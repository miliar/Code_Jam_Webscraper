import sys
from math import pi
from itertools import combinations
from operator import itemgetter

def solve_bf(data, n, k):
    max_sa = 0
    for comb in combinations(data, k):
        max_r = max(comb, key=itemgetter(0))
        sa = max_r[4]
        ind = comb.index(max_r)
        for i in range(k):
            if i == ind:
                continue
            sa += comb[i][3]
        max_sa = max(max_sa, sa)
    return max_sa

if __name__ == "__main__":
    debug_mode = True if len(sys.argv) > 1 and sys.argv[1] == "-d" else False
    if debug_mode:
        # import os
        # f = open(os.path.basename(__file__).replace(".py", ".in"))
        f = open("tmp.in")

        def input():
            return f.readline()

    t = int(input())
    for caseno in range(1, t+1):
        n, k = [int(i) for i in input().strip().split()]
        data = []
        for _ in range(n):
            r, h = [int(i) for i in input().strip().split()]
            area = pi * r * r
            circum = 2 * pi * r * h
            data.append([r, h, area, circum, area + circum])
        result = solve_bf(data, n, k)
        print("Case #{}: {}".format(caseno, result))

    if debug_mode:
        f.close()


