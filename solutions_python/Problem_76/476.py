#!/usr/bin/env python
import sys

def read_n(a):
    n = int(a[0])
    return a[1:n+1], a[n+1:]

def solve():
    N = int(sys.stdin.readline())
    data = map(int, sys.stdin.readline().split())
    even = [True]*20
    for d in data:
        i = 0
        while d:
            even[i] ^= d%2
            d //= 2
            i += 1
    
    if not all(even):
        return "NO"
    return sum(data) - min(data)


if __name__=="__main__":
    T = int(sys.stdin.readline())
    for t in range(T):
        print "Case #{}: {}".format(t+1, solve())

