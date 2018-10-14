def solve():
    n, p = map(int, raw_input().split())
    a = map(int, raw_input().split())
    c = [0] * p
    for x in a:
        c[x%p] += 1
    ans = c[0]
    memo = {tuple([0]*(p-1)): 0}
    c = c[1:]
    def go(l, k):
        if l in memo:
            return memo[l]
        p = len(l) + 1
        nc = not k
        res = 0
        for i, x in enumerate(l):
            if not x:
                continue
            nk = k + i + 1
            if nk >= p:
                nk -= p
            f = list(l)
            f[i] -= 1
            tmp = go(tuple(f), nk)
            if res < tmp:
                res = tmp
        memo[l] = res + nc
        return memo[l]
    return ans + go(tuple(c), 0)

T = int(raw_input())
for t in xrange(T):
    print "Case #%d: %d" % (t + 1, solve())
