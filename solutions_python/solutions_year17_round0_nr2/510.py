#!/usr/bin/env python3


def fuck(n):
    while True:
        s = str(n)
        l = len(s)

        gg_idx = -1
        for i in range(l-1, 0, -1):
            if s[i-1] > s[i]:
                gg_idx = i
                break

        if gg_idx == -1:
            return n

        s = s[:gg_idx] + '9' * (l-gg_idx)
        n = int(s) - 10 ** (l-gg_idx)


times = int(input())
for t in range(1, times+1):
    n = int(input())
    print(f'Case #{t}: {fuck(n)}')
