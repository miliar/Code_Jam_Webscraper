from collections import *


read_ints = lambda: [int(_) for _ in input().split()]
INF = float('INF')


def quantize(q, r):
    if 5 * q < 9 * r:
        for s in range(1, 5):
            if 9 * r * s <= 10 * q <= 11 * r * s:
                return s, s
        return None
    return (10 * q + 11 * r - 1) // (11 * r), (10 * q) // (9 * r)


def work():
    n, p = read_ints()
    rs = read_ints()
    qss = []
    for i in range(n):
        qs = []
        for q in read_ints():
            q = quantize(q, rs[i])
            if q is not None:
                qs.append(q)
        qss.append(deque(sorted(qs)))
    ans = 0
    while all(qss):
        lo = -1
        hi = INF
        for qs in qss:
            a, b = qs[0]
            lo = max(lo, a)
            hi = min(hi, b)
        if lo <= hi:
            ans += 1
            for qs in qss:
                qs.popleft()
        else:
            qs_inc = None
            for qs in qss:
                if qs_inc is None or qs[0][1] < qs_inc[0][1]:
                    qs_inc = qs
            qs_inc.popleft()
    return ans


for i in range(int(input())):
    print('Case #{}: {}'.format(i + 1, work()))
