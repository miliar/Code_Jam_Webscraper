#!/usr/bin/python3

def solve():
    n, q = list(map(int, input().split()))
    s, e, u, v = [0]*n, [0]*n, [0]*q, [0]*q
    for i in range(n):
        e[i], s[i] = list(map(int, input().split()))
    d = []
    for i in range(n):
        d.append(list(map(int, input().split())))
    for i in range(q):
        u[i], v[i] = list(map(int, input().split()))

    t = [0]*n # min time from city j to last city
    t[n-2] = d[n-2][n-1]/s[n-2]
    for j in range(n-3, -1, -1):
        t[j] = d[j][j+1]/s[j] + t[j+1]
        distance = 0
        for k in range(j+1, n):
            distance += d[k-1][k]
            if distance > e[j]:
                break
            else:
                t[j] = min(t[j], distance/s[j] + t[k])
    return t[j]

nn = int(input())
for t in range(nn):
    print('Case #{}: {}'.format(t+1, solve()))
