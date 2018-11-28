#!/usr/bin/env pypy3

def solve(s, k):
    n = len(s)
    c = 0
    for i in range(n - k + 1):
        if not s[i]:
            c += 1
            for j in range(k):
                s[i + j] = not s[i + j]
    for x in s:
        if not x:
            return "IMPOSSIBLE"
    return c

def main():
    n_tests = int(input())
    for i in range(n_tests):
        S, K = input().split(' ')
        k = int(K)
        s = list(map(lambda x: x == '+', S))
        print("Case #" + str(i + 1) + ": " + str(solve(s, k)))

main()
