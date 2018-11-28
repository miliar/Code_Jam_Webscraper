T = int(input())

for t in range(1,T+1):
    n, q = map(int, input().split())
    horses = [tuple(map(int, input().split())) for i in range(n)]
    nxt = [int(input().split()[i+1]) for i in range(n-1)]
    input()
    def dp(at, lst):
        if at == n-1:
            return 0
        new = horses[at]
        if new[0] < nxt[at] and lst[0] < nxt[at]:
            return 1e10
        if new[0] >= lst[0] and new[1] >= lst[1]:
            return nxt[at]/new[1] + dp(at+1, (new[0]-nxt[at], new[1]))
        if new[0] < nxt[at]:
            return nxt[at]/lst[1] + dp(at+1, (lst[0]-nxt[at], lst[1]))
        if lst[0] < nxt[at]:
            return nxt[at]/new[1] + dp(at+1, (new[0]-nxt[at], new[1]))
        return min(nxt[at]/new[1] + dp(at+1, (new[0]-nxt[at], new[1])), nxt[at]/lst[1] +
                dp(at+1, (lst[0]-nxt[at], lst[1])))
    for i in range(q):
        input()
    print("Case #%d: %.10f" % (t, dp(0, (0,0))))
        

