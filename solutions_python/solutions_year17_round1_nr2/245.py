from itertools import permutations as pm
from math import ceil, floor

def f(x):
    return (ceil(x / 1.1), floor(x / .9))

def okay(p, q):
    pl, pr = f(p)
    ql, qr = f(q)
    if pl > pr or ql > qr:
        return False
    return pr >= ql and qr >= pl
    
def solveSingle():
    x = int(input())
    cnt = 0
    for v in map(int, input().split()):
        ul, ur = f(v / x)
        if ul <= ur:
            cnt += 1
    return cnt

def solveDouble():
    x, y = map(int, input().split())
    b = [(v / x) for v in map(int, input().split())]
    c = [(v / y) for v in map(int, input().split())]
    ans = 0

    for xs in pm(c):
        cnt = 0
        for i, v in enumerate(b):
            if okay(v, xs[i]):
                cnt += 1
        ans = max(ans, cnt)
    return ans

t = int(input())
for i in range(1, t + 1):
    n, _ = map(int, input().split())
    a = solveSingle() if n == 1 else solveDouble()
    print('Case #%d: %d' % (i, a))
