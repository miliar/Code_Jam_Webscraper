
import sys
sys.setrecursionlimit(100000)

def solve(S, K):
    N = len(S)
    p = [i for i in xrange(N) if S[i] == '-']
    if not p:
        return 0
    end = p[0] + K
    if end > N:
        return None
    X = ''.join('+' if S[i] == '-' else '-' for i in xrange(p[0], end)) + S[end:]
    res = solve(X, K)
    return res + 1 if res is not None else res

T = int(raw_input())
for t in xrange(T):
    S, K = raw_input().split(' ')
    res = solve(S, int(K))
    print 'Case #%d: %s' % (t + 1, res if res is not None else 'IMPOSSIBLE')
