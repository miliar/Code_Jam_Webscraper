computed = {}
actual = {}

def dfs(n):
    if n==0:
        return {}
    if n in computed:
        actual[n] = {k: v*2 for k, v in computed[n].items()}
        return computed[n]
    if n % 2 == 0:
        r1 = dfs(n//2-1)
        r2 = dfs(n//2)
        computed[n] = {k: r1.get(k, 0) + r2.get(k, 0) for k in set(r1) | set(r2) }
        computed[n][n]=1
        return computed[n]
    else:
        r = dfs(n//2)
        computed[n] = { k: r.get(k, 0) + r.get(k, 0) for k in set(r) | set(r) }
        computed[n][n]=1
        return computed[n]

t = int(input())
for tc in range(t):
    n,k = map(int,input().split())
    r = dfs(n)
    r = list(reversed(sorted(r.items())))
    c = 0
    a,b = None,None
    for rr in r:
        c += rr[1]
        if c >= k:
            if rr[0] % 2 == 0:
                a,b = rr[0]//2-1,rr[0]//2
            else:
                a,b = rr[0]//2,rr[0]//2
            break
    print("Case #{}: {} {}".format(tc+1,b,a))