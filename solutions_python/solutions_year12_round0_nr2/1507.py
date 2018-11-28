from collections import defaultdict

def solve(ts, S, p):
    above = [[None] * (S+1) for _ in ts]
    for i, t in enumerate(ts):
        for s in xrange(S+1):
            if i > 0:
                prev = above[i-1][s]
            else:
                prev = 0
            ans = prev + (no_surprise[t] >= p)
            if s:
                if i > 0:
                    prev = above[i-1][s-1]
                else:
                    prev = 0
                ans = max(ans, prev+(surprise[t] >= p))
            above[i][s] = ans
    return above[-1][-1]

surprise = defaultdict(lambda: -1e100)
no_surprise = defaultdict(lambda: -1e100)
for i in xrange(11):
    for j in xrange(11):
        for k in xrange(11):
            scores = [i, j, k]
            if max(scores) - min(scores) > 2:
                continue
            elif max(scores) - min(scores) == 2:
                surprise[sum(scores)] = max(surprise[sum(scores)], max(scores))
            else:
                no_surprise[sum(scores)] = max(no_surprise[sum(scores)], max(scores))

T = int(raw_input())
for cas in xrange(1, 1+T):
    data = map(int, raw_input().split())
    N, S, p = data[:3]
    ts = data[3:]
    assert len(ts) == N
    print 'Case #%i: %i' % (cas, solve(ts, S, p))
