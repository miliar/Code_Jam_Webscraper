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
    k = input()
    n = [int(x) for x in k]

    i = len(k) - 1

    while i > 0:
        a = n[i]
        b = n[i - 1]
        if b > a:
            for j in range(i, len(n)):
                n[j] = 9
            n[i - 1] -= 1
        i -= 1
    
    print("".join(str(x) for x in n).lstrip("0"))


if __name__ == '__main__':
    solve()
