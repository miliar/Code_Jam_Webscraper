#!/usr/bin/env python3
def solve(s, k):
    s = list(map(lambda c: int(c == '+'), s))
    cnt = 0
    for i, c in enumerate(s):
        if not c and i + k <= len(s):
            cnt += 1
            for di in range(k):
                s[i+di] ^= 1
    if 0 in s:
        return 'IMPOSSIBLE'
    else:
        return cnt
t = int(input())
for x in range(t):
    s, k = input().split()
    k = int(k)
    print('Case #{}: {}'.format(x+1, solve(s, k)))

