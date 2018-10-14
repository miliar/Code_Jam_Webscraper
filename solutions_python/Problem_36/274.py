S = 'welcome to code jam'
N = int(raw_input())

def solve(s, i, j):
    if j == len(S):
        return 1
    if i == len(s):
        return 0
    
    try:
        return memo[i, j]
    except KeyError:
        v = solve(s, i+1, j)
        if s[i] == S[j]:
            v += solve(s, i+1, j+1)
        v %= 1000
        memo[i,j] = v
        return v

for cas in xrange(1, N+1):
    memo = {}
    print 'Case #%i: %04i' % (cas, solve(raw_input(), 0, 0))
