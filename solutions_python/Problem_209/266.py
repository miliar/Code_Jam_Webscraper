#!/usr/bin/env python3

PI = 3.141592653589793238

def area_top(rh):
    return rh[0] * rh[0] * PI

def area_side(rh):
    return 2 * rh[0] * rh[1] * PI

def solve(n, k, rh):
    dp = [[0] * k for _ in range(n)]
    for i in range(n):
        dp[i][0] = area_top(rh[i]) + area_side(rh[i])
    for j in range(1, k):
        for i in range(n):
            s = area_side(rh[i])
            t = area_top(rh[i])
            for l in range(i):
                x = dp[l][j - 1] + s + t - area_top(rh[l])
                if x > dp[i][j]:
                    dp[i][j] = x
    m = 0
    for i in range(n):
        if dp[i][k - 1] > m:
            m = dp[i][k - 1]
    return m

def main():
    s = input()
    t = int(s)
    for i in range(t):
        s = input()
        n, k = map(int, s.split(' '))
        rh = [0]*n
        for j in range(n):
            rh[j] = tuple(map(int, input().split(' ')))
        rh.sort()
        print("Case #" + str(i + 1) + ": " + str(solve(n, k, rh)))

main()
