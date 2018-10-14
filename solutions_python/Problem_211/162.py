t = int(input())

for q in range(t):
    n, k = map(int, input().split())
    u = float(input())
    p = list(map(float, input().split()))
    p.sort()
    np = 0
    while np < len(p)-1 and u - (np+1) * (p[np+1] - p[np]) > 0:
        u -= (np+1) * (p[np+1] - p[np])
        np += 1
    baseprob = p[np]
    np += 1

    baseprob += u / np
    r = pow(baseprob, np)
    for v in p[np:]:
        r *= v
    print("Case #{}: {:.9f}".format(q+1, r))
