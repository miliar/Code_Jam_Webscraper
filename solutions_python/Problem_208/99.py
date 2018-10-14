#!/usr/bin/env python

import sys
import logging

log = logging.getLogger(__name__)
logging.basicConfig()


class Impossible(Exception):
    pass


def print_result(result, i):
    sys.stdout.write("Case #%s: %s\n" % (i, result))


def readline():
    return sys.stdin.readline().rstrip('\n')


def splitline(f=str):
    return map(f, readline().split())


def calc_dist(i, j, dist):
    return sum(dist[i:j])


def foo(start, finish, hdist, hspeed, cdist):
    dist = []
    for i in range(finish - 1):
        dist.append(cdist[i][i+1])

    times = [None] * (finish - 1) + [0]
    for i in range(finish - 2, -1, -1):
        t = float("inf")
        # switch horses
        for j in range(i + 1, finish):
            d = calc_dist(i, j, dist)
            if hdist[i] < d:
                continue
            new = times[j] + float(d) / hspeed[i]
            t = min(t, new)
        times[i] = t
    return times[0]


def solve():
    N, Q = splitline(int)
    Es, Ss, Ds, UVs = [], [], [], []
    # Cities/Horses
    for _ in range(N):
        E, S = splitline(int)
        Es.append(E)  # Max distance
        Ss.append(S)  # Speed
    # Distances
    for _ in range(N):
        d = splitline(int)
        assert len(d) == N
        Ds.append(d)
    # Routes
    for _ in range(Q):
        U, V = splitline(int)
        UVs.append((U, V))

    res = [foo(U, V, Es, Ss, Ds) for U, V in UVs]
    return " ".join("%.30f" % r for r in res)

    return N, Q, Es, Ss, Ds, UVs
    raise Impossible


def main():
    for i in xrange(int(readline())):
        try:
            res = solve()
        except Impossible:
            res = "IMPOSSIBLE"
        print_result(res, i + 1)


if __name__ == '__main__':
    main()
