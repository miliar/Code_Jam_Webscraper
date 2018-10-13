import sys
import math

def best_prob(P, U):
    n = len(P)
    P.sort()
    for refi in range(1, len(P)):
        delta = (P[refi] - P[0]) * refi
        if delta < U:
            U -= delta
            P[0:refi] = [P[refi]] * refi
        else:
            newval = P[0] + U/refi
            P[0:refi] = [newval] * refi
            U = 0
            break
    assert len(P) == n
    if U > 0:
        p0 = P[0]
        assert P == [p0] * n
        newval = p0 + U/n
        P = [newval] * n
    ans = 1
    for p in P:
        ans *= p
    return ans


if __name__ == "__main__":
    ncases = int(sys.stdin.readline().strip())
    for i in range(ncases):
        N, K = [int(part) for part in sys.stdin.readline().split()]
        assert K == N
        U = float(sys.stdin.readline())
        P = [float(part) for part in sys.stdin.readline().split()]
        best = best_prob(P, U)
        print "Case #%d: %.9f" % (i+1, best)
