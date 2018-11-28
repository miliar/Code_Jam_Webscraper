#!/usr/bin/python3

import sys

def solve(c, f, x):
    rate = 2 # current rate
    time = 0 # time spent so far
    best = x / rate
    while True:
        # what if we buy another factory?
        time += c / rate
        rate += f
        # what if we enter the waiting phase?
        sol = time + x / rate
        best = min(sol, best)
        if time > best:
            break
    return best

t = int(sys.stdin.readline())

for case_num in range(1, t+1):
    c, f, x = map(float, sys.stdin.readline().strip().split())
    sol = solve(c, f, x)
    print("Case #%d: %.7f" % (case_num, sol))
