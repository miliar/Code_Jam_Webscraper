#!/usr/bin/env python3

import sys

def solve():
    d, n = map(int, input().split())
    maxtime = 0
    for _ in range(n):
        pos, spd = map(int, input().split())
        hours = ((d - pos) / spd)
        maxtime = max(maxtime, hours)
    return (d / maxtime)



def main():
    k = int(input())
    for i in range(k):
        print("Case #{}: {}".format(i + 1, solve()))

if __name__ == '__main__':
    main()
