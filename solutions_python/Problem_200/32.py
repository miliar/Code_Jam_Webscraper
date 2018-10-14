
def solve(S):
    N = len(S)
    for p in xrange(1, N):
        if S[p] < S[p - 1]:
            break
    else:
        return S
    v = int(S[:p]) - 1
    s = (str(v) if v else '') + '9' * (N - p)
    return solve(s)
    

T = int(raw_input())
for t in xrange(T):
    N = int(raw_input())
    res = solve(str(N))
    print 'Case #%d: %s' % (t + 1, res)
