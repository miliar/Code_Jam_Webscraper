#!/usr/bin/env python

def step(pos):
    if pos in memo:
        return memo[pos]
    profit = 0
    resp = 0
    for i in range(N):
        p = (i + pos) % N
        if profit + G[p] > K:
            break
        profit += G[p]
        resp += 1
    memo[pos] = ((resp + pos) % N, profit)
    return memo[pos]

T = int(raw_input())

for t in range(T):
    R, K, N = map(int, raw_input().split())
    G = map(int, raw_input().split())
    memo = {}

    resp = 0
    pos = 0
    visitado = [None] * 2000
    i = 0
    while R > 0:
        if visitado[pos] != None:
            break
        visitado[pos] = (i, resp)
        pos, k = step(pos)
        resp += k
        i += 1
        R -= 1
    if R > 0:
        resp += (resp - visitado[pos][1]) * (R / (i - visitado[pos][0]))
        R %= (i - visitado[pos][0])
        while R > 0:
            pos, k = step(pos)
            resp += k
            R -= 1

    print 'Case #%d: %d' %(t+1, resp)

    
