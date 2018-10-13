#!/usr/bin/env python3
from collections import defaultdict

for it in range(int(input())):
    n, k = list(map(int, input().split()))
    l, r = n, k
    cnt = defaultdict(int)
    cnt[n] = 1
    k -= 1
    while k:
        v = max(cnt.items())
        ln, vl = v
        get = min(k, vl)
        k -= get
        cnt[ln] -= get
        ch = (ln - 1) // 2
        cnt[ch] += get
        cnt[ln - 1 - ch] += get
        if not cnt[ln]:
            del cnt[ln]
    v = max(cnt.items())[0] - 1
    l, r = v // 2, (v + 1) // 2
    print('Case #{:d}: {:d} {:d}'.format(it + 1, r, l))
