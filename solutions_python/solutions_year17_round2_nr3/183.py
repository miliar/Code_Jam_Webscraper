def fastest(u, v, D, E, S, ctime, cspeed, cenergy):
    #print "{} -> {}, time{}, speed{}".format(u, v, ctime, cspeed)
    if cenergy < 0:
        return float('inf')
    if u == v:
        return ctime
    for n, d in enumerate(D[u]):
        if d < 0: 
            continue

        #no change
        a = fastest(n, v, D, E, S, ctime + (float(d)/cspeed), cspeed, cenergy - d)

        # with change
        b = fastest(n, v, D, E, S, ctime + (float(d)/S[u]), S[u], E[u] - d)
        return min(a, b)
    return float('inf')


def solve():
    N, Q = map(int, raw_input().split())
    E = []
    S = []
    for _ in range(N):
        e, s = map(int, raw_input().split())
        E.append(e)
        S.append(s)
    D = []
    for _ in range(N):
        d = map(int, raw_input().split())
        D.append(d)
    queries = []
    for _ in range(Q):
        u, v = map(int, raw_input().split())
        queries.append((u-1,v-1))

    # small
    ans = ""
    for u, v in queries:
        sol = fastest(u, v, D, E, S, 0.0, S[u], E[u])
        ans += " " + str(sol)
    return ans.strip()




T = int(raw_input())
for t in range(1, T+1):
    print "Case #{}: {}".format(t, solve())
