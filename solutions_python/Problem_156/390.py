#!/usr/bin/env python3

def solve(D, P):
    largest = max(P)
    best = D*largest
    for remaining in range(1, largest+1):
        current = sum((p-1) // remaining for p in P) + remaining
        best = min(best, current)
    return best

tests = int(input())
for test in range(tests):
    D = int(input())
    P = [int(p) for p in input().split()]
    result = solve(D, P)
    print("Case #{}: {}".format(1+test, result))
