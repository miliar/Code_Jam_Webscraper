import heapq
from collections import deque
import sys
from math import gcd


def solve():
    # sys.stdin = open('B-small-attempt0.in')
    input = sys.stdin.readline
    t = int(input())
    for x in range(t):
        n, r, o, y, g, b, v = map(int, input().split())
        # ans = 'IMPOSSIBLE'
        # if (o >= b or g >= r or v >= y):
        #     print(("Case #%d: " % (x + 1)) + ans)
        #     continue
        s = ''
        if (r >= y and r >= b):
            s = 'R'
            prev = last = 0
            r -= 1
        if (len(s) == 0 and y >= r and y >= b):
            s = 'Y'
            prev = last = 1
            y -= 1
        if (len(s) == 0 and b >= r and b >= y):
            s = 'B'
            prev = last = 2
            b -= 1
        arr = [r, y, b]
        cp = n
        n -= 2
        dct = {0: 'R', 1: 'Y', 2: 'B'}
        notFound = 0
        while n:
            n -= 1
            mx = 0
            cl = -1
            if last != prev:
                mx = arr[last]
                cl = last
            for i in range(3):
                if i != prev and mx < arr[i]:
                    mx = arr[i]
                    cl = i
            if mx == 0:
                notFound = 1
                break
            s += dct[cl]
            arr[cl] -= 1
            prev = cl
        mx = 0
        for i in range(3):
            if arr[i]:
                mx = i
        if mx == last or mx == prev or len(s) + 1 != cp:
            ans = 'IMPOSSIBLE'
        else:
            ans = s + dct[mx]
        print(("Case #%d: " % (x + 1)) + ans)


solve()
