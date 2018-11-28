def solve(P, M, prices):
    M = [P-x for x in M]
    n = len(M)
    result = 0
    for p in reversed(prices):
        if not any(M):
            break
        m = n // len(p)
        for i in xrange(0, n, m):
            if any(M[i:i+m]):
                result += 1
                for j in xrange(i, i+m):
                    if M[j]:
                        M[j] -= 1
    return result

if __name__ == '__main__':
    import sys
    rl = iter(sys.stdin).next
    for case in range(1, int(rl())+1):
        P = int(rl())
        M = map(int, rl().split())
        prices = [map(int, rl().split()) for _ in range(P)]
        print 'Case #%d: %s' % (case, solve(P, M, prices))
