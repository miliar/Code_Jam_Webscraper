#! /usr/bin/env python
cases = int(raw_input())
for case in range(0, cases):
    args = raw_input().split(' ')
    d = float(args[0])
    n = int(args[1])
    t = []
    for i in range(0, n):
        h = raw_input().split(' ')
        x = d - float(h[0])
        v = float(h[1])
        t.append(x/v)
    m = 0
    for time in t:
        if time > m:
            m = time
    ms = d/m
    print("Case #{}: {:.6f}".format(case + 1, ms))
