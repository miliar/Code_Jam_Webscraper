#!/usr/bin/env python3

################################################################################

def read_int():
    return int(input())

################################################################################

def solve(I):
    dg = [ int(x) for x in I ]
    n = len(dg)

    i = 0
    while i < n - 1 and dg[i] <= dg[i+1]:
        i = i + 1

    if i == n - 1:
        return dg

    j = i
    while j>0 and dg[j-1] == dg[j]:
        j = j - 1

    dg[j] -= 1

    for x in range(j+1,n):
        dg[x] = 9

    if dg[0] == 0:
        return dg[1:]
    
    return dg

for C in range(read_int()):
    I = input().strip()
    R = solve(I)
    print("Case #{}: {}".format(C + 1, ''.join(map(str,R))))
