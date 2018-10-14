#!/usr/bin/env python3

def get(n, div):
    return ((n % (10 * div)) - (n % div)) // div

def solve(n):
    div = 1
    while div < n:
        if get(n, 10*div) > get(n, div):
            n -= (n % (10*div)) + 1
        div *= 10

    return n

for i in range(int(input().strip())):
    n = int(input().strip())
    print("Case #{}: {}".format(i+1, solve(n)))
