#!/usr/bin/env python3

def solve(s, k):
    ans = 0
    for chunk in zip(*[range(i, len(s)) for i in range(k)]):
        if s[chunk[0]] is False:
            for c in chunk:
                s[c] = not s[c]
            ans += 1
    return ans if all(s) else 'IMPOSSIBLE'

for i in range(int(input())):
    s, k = input().split()
    print('Case #{}: {}'.format(i + 1, solve([s == '+' for s in s], int(k))))
