from math import pi

def task():
    n, k = map(int, input().split())
    p = []
    for i in range(n):
        r, h = map(int, input().split())
        p.append((h, r))
    p = sorted(p, reverse=True, key=lambda x: x[0]*x[1])

    ma = 0
    for m in p:
        p2 = list(p)
        p2.remove(m)
        total = pi * m[1] * m[1] + 2*pi*m[0]*m[1]
        p2 = [x for x in p2 if x[1] <= m[1]]
        if len(p2) < k - 1:
            continue
        for i in range(k-1):
            b = p2[i]
            total += 2*pi*b[0]*b[1]
        ma = max(ma, total)
    return "{:.100}".format(ma)

t = int(input())
for i in range(t):
    print("Case #{}: {}".format(i+1, task()))
