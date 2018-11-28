import heapq
from collections import deque
import sys
from math import gcd


def solve():
    # sys.stdin = open('A.txt')
    input = sys.stdin.readline
    t = int(input())
    for x in range(t):
        d,n = map(int, input().split())
        maxSteps = 0
        for i in range(n):
            b, u = map(int, input().split())
            maxSteps = max(maxSteps, (d - b) / u)
        print("Case #%d: " % (x + 1), end='')
        print(d / maxSteps)


solve()
