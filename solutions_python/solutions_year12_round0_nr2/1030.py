import sys

def ans(n, a):
    print 'Case #%d:'%n,
    print a

def maxn(s):
    m = s/3
    if s%3:
        m = m+1
    return m

def maxs(s):
    m = s/3
    if s%3>1:
        m = m+2
    elif m>0:
        m = m+1
    return m

def solve(N, S, p, t):
    x = 0
    for s in t:
        if maxn(s)>=p:
            x+=1
        elif S and maxs(s)>=p:
            x+=1
            S-=1
    return x

f = sys.stdin
n = int(f.readline())
for i in range(n):
    l = map(int, f.readline().split())
    N = l[0]
    S = l[1]
    p = l[2]
    t = l[3:]
    ans(i+1, solve(N,S,p,t))

