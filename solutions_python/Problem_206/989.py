#!/usr/bin/python

def algo():
    d, n = map(int, input().split())
    kp, sp = 0,0
    tmax = 0
    for i in range(n):
        k, s = map(int, input().split())
        t = (d-k) / s
        tmax = t if t > tmax else tmax
    return d/tmax;




n=int(input())
for i in range(1,n+1):
    print("Case #{}: {:.6f}".format(i, algo()))
