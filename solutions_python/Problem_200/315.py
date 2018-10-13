#!/usr/bin/env python3

import sys
import os

def solve(n) :
    l = len(n)
    n = list(map(lambda x: int(x), n))
    for i in range(l-1,0,-1):
        if n[i-1] > n[i]:
            n[i:l] = [9] * (l-i)
            n[i-1] -= 1

    return int(''.join(map(lambda x: str(x), n)))

def main():
    sys.stdin.readline()
    for i, n in enumerate(sys.stdin):
        ans = solve(n[:-1])
        print("Case #{}: {}".format(i+1, ans))

if __name__ == '__main__':
    main()
