
import heapq


def solve(t):
    N, K = map(int, raw_input().split())

    def get_key(a, b):
        m = (a+b)/2
        return -(m-a), -(b-m), a, m, b

    Q = [get_key(1, N)]
    heapq.heapify(Q)
    for _ in xrange(K-1):
        Ls, Rs, a, m, b = heapq.heappop(Q)
        Ls, Rs = -Ls, -Rs
        heapq.heappush(Q, get_key(a, m-1))
        heapq.heappush(Q, get_key(m+1, b))
    # result
    z, y, _, _, _ = heapq.heappop(Q)
    z, y = -z, -y

    print 'Case #%d: %d %d' % (t, y, z)

T = input()
for i in xrange(T):
    solve(i+1)
