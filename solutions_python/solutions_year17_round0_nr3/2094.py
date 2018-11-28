def solve(N, K):
    q = [(0, N-1)]
    while len(q) > 0:
        q.sort(key=lambda x: x[0])
        q.sort(key=lambda x: x[1]-x[0], reverse=True)

        l, r = q.pop(0)
        K -= 1

        ll = r-l+1
        if ll == 1:
            return (0, 0)

        if ll%2 == 1:
            if K == 0:
                return (ll/2, ll/2)
            q.append((l, l+ll/2-1))
            q.append((l+ll/2+1, r))
        else:
            if ll == 2:
                if K == 0:
                    return (0, 1)
                q.append((l+1, l+1))
            else:
                if K == 0:
                    return (ll/2-1, ll/2)
                q.append((l, l+ll/2-2))
                q.append((l+ll/2, r))

T = input()

for t in xrange(T):
    N, K = map(int, raw_input().split())

    left, right = solve(N, K)

    print 'Case #%d: %d %d' % (t+1, max(left, right), min(left, right))