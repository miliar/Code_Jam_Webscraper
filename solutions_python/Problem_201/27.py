
def solve(N, K):
    if N <= K:
        return 0, 0
    A = [[N, 1]]
    while K > 0:
        v, n = A.pop(0)
        r1, r2 = v / 2, (v - 1) / 2
        for x in (r1, r2):
            for t in A:
                if t[0] == x:
                    t[1] += n
                    break
            else:
                A.append([x, n])
        K -= n
    return r1, r2

T = int(raw_input())
for t in xrange(T):
    N, K = map(int, raw_input().split(' '))
    r1, r2 = solve(N, K)
    print 'Case #%d: %s %s' % (t + 1, r1, r2)
