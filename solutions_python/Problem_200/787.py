#!/usr/bin/env python3
def solve(n):
    s = str(n)
    k = 0
    for i in range(len(s)-1):
        if s[i] != s[k]:
            k = i
        if int(s[i]) > int(s[i+1]):
            left = str(int(s[:k+1])-1)
            right = '9'*len(s[k+1:])
            return int(left+right)
    return n

t = int(input())
for i in range(1, t+1):
    n = int(input())
    print('Case #{}: {}'.format(i, solve(n)))
