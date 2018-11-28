#!/usr/bin/python3

import sys

def solve(n, p, g):
    
    count = [0 for i in range(p)]
    for x in g:
        count[x % p] += 1

    ans = count[0]  # Vsi OK
    
    if p == 2:
        ans += (count[1] // 2) + (count[1] % 2)
        return ans
    
    if p == 3:
        comb = min(count[1], count[2])
    
        ans += comb
        count[1] -= comb
        count[2] -= comb
        ans += (count[1] // 3) + (1 if count[1] % 3 != 0 else 0)
        ans += (count[2] // 3) + (1 if count[2] % 3 != 0 else 0)
        return ans
    
    # p == 4
    
    # Dvojke
    ans += count[2] // 2
    count[2] %= 2
    
    # Enke in trojke
    comb = min(count[1], count[3])
    ans += comb
    count[1] -= comb
    count[3] -= comb
    
    if count[2] == 1:
        if max(count[1], count[3]) == 0:
            return ans + 1
        ans += 1
        count[1] -= 2
        count[3] -= 2
    
    if count[1] > 0:
        ans += (count[1] // 4) + (1 if count[1] % 4 != 0 else 0)
    
    if count[3] > 0:
        ans += (count[3] // 4) + (1 if count[3] % 4 != 0 else 0)
    
    return ans

t = int(sys.stdin.readline())

for i in range(1, t+1):

    n, p = map(int, sys.stdin.readline().split())
    g = [int(x) for x in sys.stdin.readline().split()]
    print("Case #{0}: {1}".format(i, solve(n, p, g)))

