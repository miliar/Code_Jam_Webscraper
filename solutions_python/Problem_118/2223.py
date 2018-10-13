#!/usr/bin/env python
from math import sqrt, ceil, floor

def fair(x):
    if x < 10: return True
    s = str(x)
    n = len(s)
    left = s[:n//2]
    right = s[ceil(n/2):][::-1]
    return left == right

def square(x):
    s = sqrt(x)
    return fair(int(s)) and floor(s)==ceil(s)

def fscount(a,b):
    ans = 0
    for x in range(a,b+1):
        if fair(x) and square(x):
            ans += 1
    return ans

if __name__ == '__main__':
    T = int(input())
    case = 1
    while case <= T:
        a,b = [int(x) for x in input().split(' ')]
        print('Case #{}: {} '.format(case, fscount(a,b)))
        case += 1
