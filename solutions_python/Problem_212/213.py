import numpy as np
from itertools import combinations
from math import ceil, floor, pi
from functools import lru_cache


def fresh_chocolate(N, P, G):
    res = 1
    p_mod = np.array([np.sum(G % P == i) for i in range(P)])

    res += p_mod[0]
    p_mod[0] = 0

    if P == 2:
        res += p_mod[1] // 2
        p_mod[1] %= 2

    elif P == 3:
        pairs_12 = min(p_mod[1], p_mod[2])
        res += pairs_12
        p_mod[1] -= pairs_12
        p_mod[2] -= pairs_12

        res += p_mod[1] // 3
        p_mod[1] %= 3

        res += p_mod[2] // 3
        p_mod[2] %= 3

    elif P == 4:
        pairs_13 = min(p_mod[1], p_mod[3])
        res += pairs_13
        p_mod[1] -= pairs_13
        p_mod[3] -= pairs_13

        p_mod[2] += p_mod[3] // 2
        p_mod[1] += p_mod[3] % 2
        p_mod[3] = 0

        pairs_22 = p_mod[2] // 2
        res += pairs_22
        p_mod[2] %= 2

        pairs_211 = min(p_mod[2], p_mod[1]//2)
        res += pairs_211
        p_mod[2] -= pairs_211
        p_mod[1] -= pairs_211*2


    print(res, p_mod)
    if sum(p_mod) == 0:
        res -= 1

    return res


if __name__ == '__main__':
    # PATH_IN = 'sample.in'
    PATH_IN = 'A-small-attempt1.in'
    # PATH_IN = 'A-large-practice.in'
    PATH_OUT = PATH_IN[:-3] + '.out'

    f_in = open(PATH_IN, 'r')
    f_out = open(PATH_OUT, 'w')

    T = int(f_in.readline())
    for t in range(T):
        line = f_in.readline().split()

        N = int(line[0])
        P = int(line[1])
        print(N, P)

        line = f_in.readline().split()
        G = np.array([float(g) for g in line])
        print(G)

        res = fresh_chocolate(N, P, G)

        print('Case #%i: %i' % (t + 1, res))
        f_out.write('Case #%i: %s\n' % (t + 1, res))
