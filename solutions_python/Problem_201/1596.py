"""
Google Code Jam
2017 Qualification Round

Problem C. Bathroom Stalls
    :author: yamaton
    :date: 2017-04-08
"""

import sys
import heapq
import collections
import functools
import itertools as it
import bisect


sys.setrecursionlimit(100000)


def get_max_min(x):
    a = x // 2
    b = x - a - 1
    return (a, b)


def solve_slow(n, k):
    h = [-n]
    heapq.heapify(h)
    for i in range(k - 1):
        interval = - heapq.heappop(h)
        a, b = get_max_min(interval)
        heapq.heappush(h, -a)
        heapq.heappush(h, -b)
    last = - heapq.heappop(h)
    res = get_max_min(last)
    return res


@functools.lru_cache(100000000)
def f(n):
    if n == 0:
        return collections.Counter({})
    elif n == 1:
        return collections.Counter({1: 1})
    else:
        a, b = get_max_min(n)
        return f(a) + f(b) + collections.Counter({n: 1})


def solve(n, k):
    res = f(n)
    acc = 0
    keys = []
    accs = []
    pairs = sorted(list(res.items()), reverse=True)
    for (key, val) in pairs:
        acc += val
        keys.append(key)
        accs.append(acc)

    idx = bisect.bisect_right(accs, k - 1)
    pp('keys', keys)
    pp('accs', accs)
    pp('len(accs)', len(accs))
    pp('len(keys)', len(keys))
    pp('idx', idx)
    next_ = keys[idx]
    pp('next =', next_)
    a, b = get_max_min(next_)
    return (a, b)


def pp(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)


def main():
    for _tc in range(1, int(input()) + 1):
        pp('\n--------- case #%d -------' % _tc)
        print("Case #%d: " % _tc, end='')
        n, k = map(int, input().split())
        result = solve(n, k)
        pp()
        pp('n, k =', (n, k))
        pp('result =', result)
        print(*result)


if __name__ == '__main__':
    main()
