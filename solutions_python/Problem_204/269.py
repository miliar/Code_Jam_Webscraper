import itertools
from collections import Counter
from itertools import *
from math import ceil, floor


def doit(target, packages):
    counts = Counter()
    for size in packages:
        a, b = ceil(size / target / 1.1), floor(size / target / 0.9)
        if a <= b:
            counts[a, b] += 1
    return counts

def solve(ingredient_targets, package_sets):
    counts = [doit(target, packages) for target, packages in zip(ingredient_targets, package_sets)]
    return s(counts)

c = {}

def s(counts, kits=0):
    h = tuple(tuple(c.items()) for c in counts)
    if h not in c:
        c[h] = _s(counts)
    return c[h] + kits


def _s(counts, kits=0):
    if not any(counts):
        return kits
    for k in counts[0].keys():
        if all(k in count for count in counts):
            n = min(count[k] for count in counts)
            sub = Counter({k: n})
            return s([count - sub for count in counts], kits + n)
        a, b = k
        if all(any(a <= b0 and a0 <= b for a0, b0 in count.keys()) for count in counts):
            for i in range(a, b + 1):
                if all(any(a0 <= i <= b for a0, b0 in count.keys()) for count in counts):
                    candidates = [{(a0, b0) for a0, b0 in count.keys() if a <= b0 and a0 <= b} for count in counts[1:]]
                    return kits + without(counts, [{k}] + candidates)
    return kits

def without(counts, choices):
    return max(f(counts, spans)
               for spans in itertools.product(*choices)) + 1

def f(counts, spans):
    # n = min(count[span] for count, span in zip(counts, spans))
    n = 1
    assert n > 0
    return s([count - Counter({span: n}) for count, span in zip(counts, spans)])

# solve([500, 300], [[900], [660]])
# solve([500, 300], [[1500], [809]])
# solve([50, 100], [[450, 449], [1100, 1101]])
# solve([500, 300], [[300], [500]])
# solve([10], [[11, 13, 17, 11, 16, 14, 12, 18]])
# solve([70, 80, 90], [[1260, 1500, 700], [800, 1440, 1600], [1700, 1620, 900]])

T = int(input())
for t in range(T):
    N, P = map(int, input().split())
    R = list(map(int, input().split()))
    Q = [list(map(int, input().split())) for _ in range(N)]
    print('Case #%d: %d' % (t + 1, solve(R, Q)))
