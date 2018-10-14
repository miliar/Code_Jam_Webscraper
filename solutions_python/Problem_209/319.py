#NTheo
from __future__ import division
from math import pi

T = int(raw_input())
for t in range(T):
    N, K = [int(x) for x in raw_input().split()]
    pancakes = [[int(x) for x in raw_input().split()] for _ in xrange(N)]
    pw = max(pancakes, key=lambda p: 2*p[0]*p[1]+p[0]*p[0])
    selected = [pw]
    pancakes.remove(pw)
    pancakes.sort(key = lambda p: 2*p[0]*p[1], reverse=True)
    selected += pancakes[:K-1]
    w = 2 * pi * sum([p[0] * p[1] for p in selected]) + pi * max(selected, key=lambda p: p[0])[0]**2
    print('Case #{}: {}'.format(t+1, w)) 
    
    