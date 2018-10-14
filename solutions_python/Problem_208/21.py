import sys


def compute(N, Q, D, E, S):
    best = [-2] * N
    best[0] = 0
    for i in xrange(N):
        for j in xrange(i + 1, N):
            if D[j] - D[i] > E[i]:
                continue
            t = best[i] + float(D[j] - D[i]) / S[i]
            if best[j] < -1 or t < best[j]:
                best[j] = t
    return "%.8f" % best[N - 1]


def parse():
    N, Q = map(int, sys.stdin.readline().strip().split())
    E = []
    S = []
    for i in xrange(N):
        e, s = map(int, sys.stdin.readline().strip().split())
        E.append(e)
        S.append(s)
    D = [0]
    for i in xrange(N):
        dij = map(int, sys.stdin.readline().strip().split())
        if i + 1 < N:
            D.append(D[i] + dij[i + 1])
    for i in xrange(Q):
        uv = sys.stdin.readline()
    return N, Q, D, E, S



if __name__ == "__main__":
    sys.setrecursionlimit(100000)
    T = int(sys.stdin.readline().strip())
    for i in xrange(T):
        data = parse()
        result = compute(*data)
        print "Case #%d: %s" % (i + 1, result)
