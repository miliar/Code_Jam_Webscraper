import sys


def check(a, b, R):
    n1 = (a / 1.1) / R[0]
    n2 = (a / 0.9) / R[0]
    n1 = int(n1) - 3
    n2 = int(n2) + 3
    for n in xrange(n1, n2):
        if n * R[0] * 9 <= 10 * a and n * R[0] * 11 >= 10 * a:
            if n * R[1] * 9 <= 10 * b and n * R[1] * 11 >= 10 * b:
                return True
    return False


def compute(N, P, R, Q):
    if N > 2:
        return -1
    if N == 1:
        total = 0
        for i in xrange(P):
            if check(Q[0][i], Q[0][i], [R[0], R[0]]):
                total += 1
        return total
    for i in xrange(N):
        Q[i] = sorted(Q[i])
    j = 0
    used = set()
    for i in xrange(P):
        for j in xrange(P):
            if j in used:
                continue
            if check(Q[0][i], Q[1][j], R):
                used.add(j)
                break
    return len(used)


def parse():
    N, P = map(int, sys.stdin.readline().strip().split())
    R = map(float, sys.stdin.readline().strip().split())
    Q = []
    for i in xrange(N):
        Q.append(map(float, sys.stdin.readline().strip().split()))
    return N, P, R, Q


if __name__ == "__main__":
    sys.setrecursionlimit(100000)
    T = int(sys.stdin.readline().strip())
    for i in xrange(T):
        data = parse()
        result = compute(*data)
        print "Case #%d: %s" % (i + 1, result)
