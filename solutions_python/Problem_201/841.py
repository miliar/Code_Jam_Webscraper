from collections import defaultdict
from math import log2


def f(n, k):
    d = defaultdict(lambda: 0)
    d[n] += 1

    while k:
        key = max(d.keys())
        kk = min(d[key], k)
        k -= kk
        d[key] -= kk
        if not d[key]:
            del d[key]
        key -= 1
        d[key // 2] += kk
        d[key - key // 2] += kk
    return '%s %s' % (key - key // 2, key // 2)


for _ in range(int(input())):
    a, b = map(int, input().split())
    print('Case #%s: %s' % (_ + 1, f(a, b)))
