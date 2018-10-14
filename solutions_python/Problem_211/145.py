import heapq
T = int(input())
for x in range(1, T + 1):
    N, K = map(int, input().split())
    U = float(input())
    Ps = list(map(float, input().split()))
    dict = {}
    for p in Ps:
        if p in dict:
            dict[p] += 1
        else:
            dict[p] = 1
    Qs = list(sorted(set(Ps)))
    cnt = 0
    while 1e-9 < U and cnt < 1000000:
        p = Qs[0]
        Qs = Qs[1:]
        q = min(U / dict[p], (Qs[0] if 0 < len(Qs) else 1.0) - p)
        U -= q * dict[p]
        if p + q in dict:
            dict[p + q] += dict[p]
        else:
            Qs.append(p + q)
            dict[p + q] = dict[p]
        del dict[p]
        Qs = list(sorted(Qs))
        cnt += 1
    ans = 1.0
    for p, r in dict.items():
        ans *= p ** r
    print("Case #%d: %f" % (x, ans))
