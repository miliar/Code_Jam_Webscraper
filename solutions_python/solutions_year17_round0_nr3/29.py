from collections import defaultdict as dd
T = int(input())
for t in range(1,T+1):
    N, K = [ int(_) for _ in input().split() ]
    Q = dd(int,{N:1})
    while K > 0:
        L, C = max(Q.items())
        del Q[L]
        A, B, K = (L-1)//2, L//2, K-C
        if K <= 0: print('Case #{}: {} {}'.format(t,B,A))
        Q[A] += C
        Q[B] += C
