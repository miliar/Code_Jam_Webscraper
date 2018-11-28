#!/usr/bin/python3

import sys

def solve(C, F, X, rate, time):

    if C/rate+X/(rate+F) >= X/rate:
        return time+X/rate

    return min(solve(C, F, X, rate+F, time+C/rate), time+X/rate)


if __name__ == "__main__":

    sys.setrecursionlimit(2000)

    T = int(sys.stdin.readline())

    for case in range(T):

        [C, F, X] = [float(X) for X in sys.stdin.readline().split()]

        Ans = solve(C, F, X, 2.00, 0.0)

        print("Case #", case+1, ": ", Ans, sep="")

