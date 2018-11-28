#!/usr/bin/env python3
pr = lambda n, m, o : print("Case #{}: {} {}".format(n,m,o))

T = int(input())
for i in range(T):
    inp = input().split(" ")
    N = int(inp[0])
    K = int(inp[1])
    avail = { N : 1 } 
    k = 0
    if (N == K): 
        pr(i+1, 0, 0)
        continue
    while k < K:
        c = max(avail)
        num = avail[c]
        k += num
        if c%2 == 0:
            lhs = (c//2)-1
            rhs = (c//2)
        else:
            lhs = (c-1)//2
            rhs = lhs
        if lhs > 0:
            if lhs in avail and lhs > 0:
                avail[lhs] += num
            else:
                avail[lhs] = num
        if rhs > 0:
            if rhs in avail:
                avail[rhs] += num
            else:
                avail[rhs] = num
        del avail[c]
        if (k+1 > K):
            pr(i+1, rhs, lhs)
        
    

