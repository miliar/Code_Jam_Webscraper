import heapq as hq


def check(D, N, Ks, Ss, v):
    rtn = True
    for i in range(N):
        K = Ks[i]
        S = Ss[i]
        if K + S * D / v < D:
            rtn = False
            break
    return rtn

T = int(input())
for t in range(1, T + 1):
    D, N = map(int, input().split())
    Ks = []
    Ss = []
    for i in range(N):
        K, S = map(int, input().split())
        Ks.append(K)
        Ss.append(S)

    eps = 1e-10
    l = 1.0
    r = 1e18
    cnt = 0
    while eps < r - l and cnt < 1000:
        cnt += 1
        c = (l + r) / 2.0
        if check(D, N, Ks, Ss, c):
            l = c
        else:
            r = c
    ans = l
    print("Case #%d: %f" % (t, ans))
