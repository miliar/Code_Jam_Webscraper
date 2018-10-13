#!/usr/bin/python3

def solve():
    d,n = list(map(int, input().split()))
    s = [0]*n
    k = [0]*n
    for i in range(n):
        k[i],s[i] = list(map(int, input().split()))
    slowest = n-1
    t_slowest = (d-k[n-1])/s[n-1]
    for i in range(n-2, -1, -1):
        t_next = (d-k[i])/s[i]
        if t_next > t_slowest:
            slowest = i
            t_slowest = t_next
    return d/t_slowest

nn = int(input())
for t in range(nn):
    print('Case #{}: {}'.format(t+1, solve()))
