def product(l):
    p = 1
    for i in l:
        p *= i
    return p


t = int(input())
for lol in range(1, t + 1):
    n, k = [int(e) for e in input().split(" ")]
    u = float(input())
    P = [float(e) for e in input().split(" ")]
    P.sort(key=lambda l: l)
    s = 0
    i = 1
    while i < n and s + (P[i] - P[i - 1]) * i < u:
        s += (P[i] - P[i - 1]) * i
        for k in range(0, i):
            P[k] = P[i]
        i += 1
    for k in range(0, i):
        P[k] += (u - s) / i
    M = min(product(P), 1)
    print("Case #{}: {}".format(lol, M))
