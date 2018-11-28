
def f(u, s, d):
    if u==N-1:
        return 0
    if d in cache[u][s]:
        return cache[u][s][d];
    res = 10**18
    if d>=g[u][u+1]:
        cost = f(u+1, s, d-g[u][u+1]) + g[u][u+1]/s
        res = min(res, cost)
    if H[u][0]>=g[u][u+1]:
        cost = f(u+1, H[u][1], H[u][0]-g[u][u+1]) + g[u][u+1]/H[u][1]
        res = min(res, cost)
    cache[u][s][d] = res
    return res


for t in range(int(input())):
    N, Q = map(int, input().split())
    H = [tuple(map(int, input().split())) for i in range(N)]
    g = [list(map(int, input().split())) for i in range(N)]
    q = [tuple(map(int, input().split())) for i in range(Q)]


    cache = [[{} for i in range(1001)] for j in range(N)]
    ans = f(0, 0, 0)

    print('Case #{}: {}'.format(t+1, ans))