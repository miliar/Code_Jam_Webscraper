#!/usr/bin/python3
t = int(input())

for it in range(1, t+1) :
    D, N = [int(i) for i in input().split()]
    mt = 0
    for _ in range(N):
        x, v = [int(i) for i in input().split()]
        t = (D - x) / v
        mt = max(t, mt)
    ans = D / mt
    print("Case #%d:"%it, ans)
