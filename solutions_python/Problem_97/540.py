# -*- coding: utf-8 -*-

from __future__ import print_function

import math


def shift(i):
    rank = int(math.trunc(math.log(i, 10)))

    acc, m, d = 1, 0, i
    while d and not m:
        acc *= 10
        d, m = divmod(i, acc)

    return m * (10 ** (rank + 1) // acc) + d


def count(x, y):
    seen, count = set(), 0

    for i in xrange(x, y + 1):
        j = i

        while True:
            j = shift(j)

            if i == j:
                break

            if j < x or j > y:
                continue

            if (i, j) in seen or (j, i) in seen:
                break

            count += 1
            seen.add((i, j))

    return count


if __name__ == "__main__":
    n = int(raw_input())
    for i in xrange(1, n + 1):
        x, y = map(int, raw_input().split())
        print("Case #{0}: {1}".format(i, count(x, y)))
