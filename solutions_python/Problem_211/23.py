from decimal import Decimal

def task(tid):
    n, k = map(int, input().split())
    u = Decimal(input())
    ps = sorted(map(Decimal, input().split()))
    rep = 0
    while u > 0 and rep < 10000:
        rep += 1
        c = 0
        v = ps[0]
        tv = Decimal(1) 
        for i in range(n):
            if ps[i] == v:
                c += 1
            else:
                tv = ps[i]
                break
        increase = min(tv - v, u / Decimal(c))
        u -= increase * c
        for i in range(c):
            ps[i] += increase
    result = Decimal(1.0)
    for p in ps:
        result *= p
    return result


t = int(input())
for i in range(t):
    print("Case #{}: {}".format(i+1, task(i)))
