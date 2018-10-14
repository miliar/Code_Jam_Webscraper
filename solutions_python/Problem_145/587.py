from decimal import Decimal
from math import log
from sys import stdin

def solve(p, q):
    lo = log(Decimal(q), 2)
    pq = Decimal(p) / Decimal(q)
    x = Decimal(1)
    res = -1
    for i in range(1, 40):
        x *= Decimal(2)
        ox = Decimal(1) / x
        if pq >= ox:
            if res == -1:
                pq -= ox
                res = i
            else:
                pq -= ox
    if pq != 0:
        res = "Impossible"
    return res

t = int(stdin.readline())
for i in range(1, t+1):
    [p, q] = [int(x) for x in stdin.readline().split('/')]
    print("Case #{}: {}".format(i, solve(p, q)))
