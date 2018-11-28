#!/bin/env python

def print_case(n, s):
    print("Case  #%d: %s" % (n, s))

def solve(n):
    C, F, X = [float(i) for i in raw_input().split()]
    ps = 2
    time_spend = 0
    while 1:
        t1 = X / ps
        t2 = C / ps + X / (ps + F)
        if t1 <= t2:
            print_case(n, "%.7f" % (time_spend + t1))
            return
        time_spend += C / ps
        ps += F

if __name__ == '__main__':
    N = int(raw_input())
    for i in range(N):
        solve(i + 1)
