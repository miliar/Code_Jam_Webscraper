from itertools import permutations
from fractions import Fraction


def solve():
    N, P = map(int, raw_input().split())
    R = map(int, raw_input().split())
    Q = [map(int, raw_input().split()) for _ in xrange(N)]

    def limit(n, k):
        return Fraction(10*Q[n][k], 11*R[n]), Fraction(10*Q[n][k], 9*R[n])

    ans = 0

    if (N == 1):
        for i in xrange(P):
            l, r = limit(0, i)
            for j in xrange(int(l), int(r)+1):
                if l <= j and j <= r:
                    ans += 1
                    break
        return ans

    for p in permutations(range(P)):
        tmp = 0
        for i in xrange(P):
            l1, r1 = limit(0, i)
            l2, r2 = limit(1, p[i])
            for j in xrange(int(max(l1, l2)), int(min(r1, r2))+1):
                if max(l1, l2) <= j and j <= min(r1, r2):
                    tmp += 1
                    break
        ans = max(tmp, ans)

    return ans

if __name__ == '__main__':
    T = input()
    for t in xrange(1, T+1):
        print "Case #%d: %d" % (t, solve())
