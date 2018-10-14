#NTheo
from __future__ import division

T = int(input())
for t in range(T):
    D, N = [int(x) for x in input().split()]
    w = float('inf')
    for n in range(N):
        K, S = [int(x) for x in input().split()]
        w = min(w, D/((D-K)/S))
    print('Case #{}: {}'.format(t+1, w))