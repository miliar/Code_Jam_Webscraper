#!/usr/bin/python3

PI = 3.14159265358979323846264338327950288

T = int(input())

for case in range(1, T+1):
    maxSurface = -1
    N, K = map(int, input().split())
    pancakes = [None] * N
    for i in range(N):
        pancakes[i] = tuple(map(int, input().split()))
    pancakes.sort(key = lambda tup: tup[0])

    for i in range(K, N+1):
        firsts = sorted(pancakes[:i-1], key = lambda tup: tup[0] * tup[1], reverse=True)
        surface = pancakes[i-1][0]**2 + 2*pancakes[i-1][0]*pancakes[i-1][1]
        surface += sum(map(lambda tup: 2*tup[0]*tup[1], firsts[:K-1]))
        maxSurface = max(surface, maxSurface)

    print("Case #" + str(case) + ": " + str(PI * maxSurface))
    
