import os  # NOQA
import sys  # NOQA
import re  # NOQA
import math  # NOQA
import operator
from collections import Counter, deque, namedtuple  # NOQA
from functools import reduce
from itertools import count, product, permutations, combinations, combinations_with_replacement  # NOQA

# Itertools Functions:
# product('ABCD', repeat=2)                   AA AB AC AD BA BB BC BD CA CB CC CD DA DB DC DD
# permutations('ABCD', 2)                     AB AC AD BA BC BD CA CB CD DA DB DC
# combinations('ABCD', 2)                     AB AC AD BC BD CD
# combinations_with_replacement('ABCD', 2)    AA AB AC AD BB BC BD CC CD DD

EPSILON = 10 ** -8


def mul(lst):
    """Like sum(), but for multiplication."""
    return reduce(operator.mul, lst, 1)  # NOQA


for case in range(1, int(input()) + 1):
    res = None
    n, k = (int(x) for x in input().split())
    u = float(input())
    probs = [float(x) for x in input().split()]

    probs.sort()
    # print(probs)

    while u > 0:
        if all(p >= 1 for p in probs):
            break

        if u < EPSILON:
            break

        base = probs[0]
        # print(base)
        num = sum(1 for p in probs if p == base)

        amt = min(1 - base, u / num)

        if num < len(probs):
            amt = min(amt, probs[num] - base)

        for i in range(num):
            probs[i] += amt

        u -= amt * num

        probs.sort()
        # print(probs, u)


    # print(probs)
    res = mul(probs)


    print("Case #{}: {:.8f}".format(case, res))
