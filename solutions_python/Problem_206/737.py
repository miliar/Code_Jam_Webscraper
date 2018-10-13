#!/usr/bin/env python3
t = int(input())

for case in range(1, t+1):
    d, n = map(int, input().split())
    horses = []
    for _ in range(n):
        k, s = map(int, input().split())
        horses.append((k,s))
    horses = sorted(horses, reverse=True)
    time = 0
    for i, (k, s) in enumerate(horses):
        req = d-k
        if req > 0:
            time = max(time, req/s)
    print('Case #{}: {}'.format(case, d/time))
