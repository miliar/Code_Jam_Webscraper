#!/usr/bin/env python3

T = int(input())
for t in range(T):
    M, S = input().split()
    M = int(M)
    assert len(S) == M + 1
    S = [int(x) for x in S]
    needed = 0
    standing = 0
    for i, count in enumerate(S):
        if standing < i:
            needed += i - standing
            standing = i
        standing += count
    print('Case #{}: {}'.format(t+1, needed))
