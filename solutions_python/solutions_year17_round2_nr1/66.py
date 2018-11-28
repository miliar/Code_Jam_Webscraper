#!/usr/bin/env python3

T = int(input())

for case in range(1, T + 1):
    D, N = map(int, input().split())
    horses = []
    for i in range(N):
        k, s = map(int, input().split())
        horses.append((k, s))
    max_time = 0
    for k, s in horses:
        time = (D - k)/s
        max_time = max(time, max_time)
    answer = D / max_time
    print("Case #", case, ": ", answer, sep="")
