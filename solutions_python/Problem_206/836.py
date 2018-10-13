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
    d, n = map(int, input().split())  # dest position, number of horses
    horses = []
    for _ in range(n):
        k, s = map(int, input().split())  # initial position, maximum speed
        horses.append((k, s))

    def time_to_go(k, s):
        dist = d - k
        t = dist / s
        return t

    max_time = max(time_to_go(k, s) for k, s in horses)

    speed = d / max_time

    print(speed)

if __name__ == '__main__':
    solve()
