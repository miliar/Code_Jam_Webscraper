#!/usr/bin/env python
import sys

T = int(input())
for case in range(1, T + 1):
    a = []
    ra = int(input()) - 1
    for i in range(4):
        row = list(map(int, input().split()))
        a.append(row)
    b = []
    rb = int(input()) - 1
    for i in range(4):
        row = list(map(int, input().split()))
        b.append(row)
    k = 0
    ans = 0
    for x in a[ra]:
        for y in b[rb]:
            if x == y:
                k += 1
                ans = x
    if k == 0:
        print("Case #" + str(case) + ": Volunteer cheated!")
    elif k == 1:
        print("Case #" + str(case) + ": " + str(ans))
    else:
        print("Case #" + str(case) + ": Bad magician!")
