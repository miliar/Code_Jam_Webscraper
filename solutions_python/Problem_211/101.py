from functools import reduce
import operator

t = int(input())

for tc in range(1, t+1):
    n, k = map(int, input().split())
    u = float(input())
    p = sorted(map(float, input().split()))

    #if sum(p)+u >= n:
    #    print("Case #{}: {}".format(tc, 1))
    #    continue

    prev = 0
    for c, a in enumerate(p):
        if c * (a - prev) <= u:
            u -= c* (a-prev)
            prev = a
        else:
            prev += u/c
            for i in range(c):
                p[i]=prev
            u=0
            break
    if u>0:
        prev += u/n
        for i in range(n):
            p[i]=prev
    res = float(reduce(operator.mul, p, 1))
    print("Case #{}: {}".format(tc, res))
