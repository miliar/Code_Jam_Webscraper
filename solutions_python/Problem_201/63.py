#!/usr/bin/env python

fin = open("3.in", "r")
fout = open("3.out", "w")

T = int(fin.readline())
for t in range(T):
    print t+1
    N, K = map(int, fin.readline().split())
    gaps = {}
    gaps[N] = 1

    max_gap = N
    while max_gap > 0:
        # split all gaps of size max_gap
        splits = gaps.pop(max_gap, None)
        small_gap = (max_gap - 1) / 2
        large_gap = max_gap / 2
        if K <= splits:
            ans = (large_gap, small_gap)
            break
        K -= splits
        if small_gap not in gaps:
            gaps[small_gap] = 0
        if large_gap not in gaps:
            gaps[large_gap] = 0

        gaps[small_gap] += splits
        gaps[large_gap] += splits
        max_gap = max(gaps.keys())

    ans = ' '.join(map(str, ans))
    fout.write("Case #" + str(t+1) + ": " + ans + "\n")
