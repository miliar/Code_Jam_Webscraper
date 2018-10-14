t = int(input())
for q in range(t):
    d, n = map(int, input().split())

    tmax = 0.0
    for i in range(n):
        k, s = map(int, input().split())
        if k >= d: continue
        tmax = max(tmax, (d-k) / s)

    S = d / tmax
    print("Case #{}: {:.6f}".format(q+1, S))
