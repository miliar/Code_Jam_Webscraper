#!/usr/bin/python

def ir(): return int(raw_input())

def flip(e):
    if e == '+': return '-'
    else       : return '+'

def solve():
    I = "IMPOSSIBLE"
    s = raw_input().split(); s, K = s; K = int(K); s = list(s)

    i = ans = 0; n = len(s)
    while True:
        if i == n: break
        if s[i] == '+': i += 1; continue
        for j in range(i, i + K):
            if j > n - 1: return I
            s[j] = flip(s[j])
        ans += 1
    return ans

T = ir()
for it in xrange(1, T+1):
    ans = solve()
    print "Case #%d:" % it, ans
