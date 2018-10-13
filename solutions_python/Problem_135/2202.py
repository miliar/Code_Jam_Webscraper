#!/usr/bin/env python3

import sys

T = int(sys.stdin.readline().strip())
N = 4

for t in range(T):
    r1 = int(sys.stdin.readline().strip())
    i = 1
    while i < r1:
        sys.stdin.readline()
        i += 1
    row1 = sys.stdin.readline().strip().split()
    while i < N:
        sys.stdin.readline()
        i += 1
    
    r2 = int(sys.stdin.readline().strip())
    i = 1
    while i < r2:
        sys.stdin.readline()
        i += 1
    row2 = sys.stdin.readline().strip().split()
    while i < N:
        sys.stdin.readline()
        i += 1
    
    row1 = set(row1)
    row2 = set(row2)
    common = row1 & row2
    if len(common) == 0:
        res = "Volunteer cheated!"
    elif len(common) > 1:
        res = "Bad magician!"
    else:
        res = common.pop()
    print("Case #{}: {}".format(t+1, res))

