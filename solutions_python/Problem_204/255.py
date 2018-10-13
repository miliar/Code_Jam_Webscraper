#!/usr/bin/python3

import sys
import math
from functools import reduce

def solve(nb_ing, nb_packs, R, Q):
    v = [0] * nb_ing

    for q in Q:
        q.sort()

    nb_sets = 0
    while True:
        ratio = []
        if max(v) >= nb_packs:
            return nb_sets

        for i in range(nb_ing):
            r = R[i]
            f = Q[i][v[i]] / r
            fr = int(round(f))
            ratio.append(fr)

        for pp in range(min(ratio), max(ratio) + 1):
            valid = True
            for i in range(nb_ing):
                p = R[i] * pp
                if 0.9 * p <= Q[i][v[i]] and Q[i][v[i]] <= 1.1 * p:
                    pass
                else:
                    valid = False
            if valid:
                break

        if valid:
            nb_sets += 1
            nb_packs -= 1
            if nb_packs == 0:
                return nb_sets
            for i in range(nb_ing):
                del Q[i][v[i]]
            continue

        if max(v) >= nb_packs:
            return nb_sets

        p = v.index(min(v))
        if v[p] < nb_packs - 1:
            v[p] += 1
        else:
            return nb_sets

    return nb_sets

def main():
    nb = int(get_line())
    for case_id in range(1, nb + 1):
        l = get_line()
        N = int(l.split(' ')[0])
        P = int(l.split(' ')[1])
        R = [int(v) for v in get_line().split(' ')]
        Q = [[int(v) for v in get_line().split(' ')] for x in range(N)]


        ret = solve(N, P, R, Q)

        print('Case #%d: %d' %(case_id, ret), file = o)

def get_line():
    return f.readline().strip()

def open_files():
    if len(sys.argv) == 1:
        f = sys.stdin
        o = sys.stdout

    if len(sys.argv) == 2:
        f = open(sys.argv[1], 'r')
        o = sys.stdout

    if len(sys.argv) == 3:
        f = open(sys.argv[1], 'r')
        o = open(sys.argv[2], 'w')

    return (f, o)

if __name__ == "__main__":
    (f, o) = open_files()
    main()

