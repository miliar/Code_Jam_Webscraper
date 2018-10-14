#!python
import sys
from math import pi

def solve(n, k, pan):
    pan.sort()
    pan.reverse()
    cache = {}
    
    def dp(i, j, r):
        if (i,j, r) in cache:
            return cache[(i,j,r)]
        if j == 0:
            return 0
        if i >= n:
            return -100000
        p = pan[i]
        if r == 0:            
            a1 = top(p)+side(p)+dp(i+1, j-1, p[0])
            a2 = dp(i+1, j, r)
            cache[(i,j,r)] = max(a1,a2)
        else:
            a1 = side(p)+dp(i+1, j-1, p[0])
            a2 = dp(i+1, j, r)
            cache[(i,j,r)] = max(a1,a2)
        return cache[(i,j,r)]
        
    return dp(0, k, 0)
    
def top(p):
    return pi*p[0]*p[0]

def side(p):
    return 2*pi*p[0]*p[1]

def main():
    t = int(input())
    for c in range(1, t + 1):
        n, k = map(int, input().split(' '))
        pan = []
        for _ in range(n):
            r, h = map(int, input().split(' '))
            pan.append((r,h))
        res = solve(n, k, pan)
        print('Case #%d: %f' % (c, res))
    
if __name__ == "__main__":
  sys.setrecursionlimit(10000)
  main()
    