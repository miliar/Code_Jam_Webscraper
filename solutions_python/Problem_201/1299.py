from heapq import *
from sys import stdin

def f(interval):
    a, b = interval
    return [x for x in [(a, a+(b-a+1)//2-1), (a+(b-a+1)//2, b)] if x[0] < x[1]]

def l(interval):
    a, b = interval
    return b - a

def v(interval):
    return (N-l(interval), interval[0], interval)

def solve(N, K):
    interval = (0, N)
    lst = [(0, 0, (0, N))]

    for _ in range(K-1):
        x = heappop(lst)

        for e in f(x[2]):
            heappush(lst, v(e))

    r = heappop(lst)

    return (l(r[2]))//2, (l(r[2])-1)//2

T = int(next(stdin))

for t in range(1, T+1):
    N, K = map(int, next(stdin).strip().split(" "))

    print("Case #{0}: {1} {2}".format(t, *solve(N, K)))
