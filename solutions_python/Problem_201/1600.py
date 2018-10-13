#!/usr/bin/python3

def solve(n,k):
    if k == 0:
        return 0, n
    minL = int((n-1)/2)
    maxL = int(n/2)
    if k == 1:
        return maxL, minL
    k = k - 1
    return solve(maxL, int(k/2 + 0.5)) if k % 2 == 1 else solve(minL, int(k/2 + 0.5)) 

s = int(input())
for t in range(s):
    n,k = list(map(int, input().split()))
    print('Case #{0}: {1[0]} {1[1]}'.format(t+1, solve(n, k)))
