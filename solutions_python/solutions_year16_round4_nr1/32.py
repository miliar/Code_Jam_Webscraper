def solve():
    n, r, p, s = map(int, raw_input().split())
    xt = {'R': 'RS', 'P': 'PR', 'S': 'PS'}
    res = ""
    for c in 'PRS':
        l = c
        for j in xrange(n):
            l = [xt[x] for x in l]
            while len(l) > 1:
                l = [(l[k] + l[k+1]) if l[k] < l[k+1] else (l[k+1] + l[k]) for k in xrange(0, len(l), 2)]
            l = l[0]
        if l.count('R') == r and l.count('P') == p and l.count('S') == s:
            if not res or res > l:
                res = l
    if res:
        return res
    return "IMPOSSIBLE"

T = int(raw_input())
for t in xrange(T):
    print "Case #%d:" % (t + 1), solve()
