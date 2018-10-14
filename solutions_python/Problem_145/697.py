import math
import fractions
T = int(input())
for t in range(1, T+1):
    p,q = map(int, input().split('/'))
    g = fractions.gcd(p,q)
    p //= g
    q //= g
    plog = math.floor(math.log(p, 2))
    qlog = math.log(q, 2)
    qflog = math.floor(qlog)
    if (qlog != qflog):
        ans = "impossible"
    else:
        ans = qflog-plog
    print("Case #{}: {}".format(t, ans))
