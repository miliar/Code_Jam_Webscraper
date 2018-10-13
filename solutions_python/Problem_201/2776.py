import os
import re
import sys
import math
import time
import bisect
import random
import datetime
import itertools
import functools
import collections
from contextlib import contextmanager


def debug(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)


def solve():
    nb = int(input())

    debug("[START] %d cases to solve:" % nb)

    total = 0

    for i in range(1, nb + 1):
        print("Case #%d:" % i, end=" ")

        start = time.process_time()
        solve_case()
        end = time.process_time()

        t = end - start
        total += t

        m, s = divmod(total, 60)

        debug("[%d:%02.02f] Case #%d solved in %.02f seconds" % (m, s, i, t))

    debug("[END] All cases solved")


def solve_case():
    n, k = map(int, input().split())
    occupied = [0, n + 1]
    for i in range(k):
        best_mini, best_maxi, best_pos = -math.inf, -math.inf, math.inf
        for a, b in zip(occupied, occupied[1:]):
            pos = (a + b) // 2
            ls, rs = pos - a - 1, b - pos - 1
            mini, maxi = min(ls, rs), max(ls, rs)
            if mini > best_mini or (mini == best_mini and maxi > best_maxi) or (mini == best_mini and maxi == best_maxi and pos < best_pos):
                best_mini, best_maxi, best_pos = mini, maxi, pos
        occupied.append(best_pos)
        occupied.sort()

    print(best_maxi, best_mini)




if __name__ == '__main__':
    solve()
