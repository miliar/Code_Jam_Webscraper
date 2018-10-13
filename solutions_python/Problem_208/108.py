#def solve(E, S, D, UV):
from functools import wraps

def memoize(function):
    memo = {}
    @wraps(function)
    def wrapper(*args):
        if args in memo:
            return memo[args]
        else:
            rv = function(*args)
            memo[args] = rv
            return rv
    return wrapper

def solve_small(N, E, S, D):
    U = 0
    V = N-1
    e = E[U]
    s = S[U]
    d = D[0][1]
    t = d/s + find_shortest(1, e-d, s, V, E, S, D)
    #print 'end: ', i, d, e, s, d/s, t
    return t

@memoize
def find_shortest(i, e, s, V, E, S, D):
    #print i, e, V
    if i==V:
        return 0.
    res = []
    d = D[i][i+1]
    if d < 0:
        return 1e11
    if E[i] >= d:
        res.append(d/S[i] + find_shortest(i+1, E[i]-d, S[i], V, E, S, D))
    if e >= d:
        res.append(d/s + find_shortest(i+1, e-d, s, V, E, S, D))
    #print 'end: ', i, d, e, s, res, d/s + min(res)
    return min(res)


if __name__ == '__main__':
    T = int(raw_input())
    for t in range(1, T+1):
        N, Q = map(int, raw_input().split())
        E = []
        S = []
        for i in range(N):
            Ei, Si = map(int, raw_input().split())
            E.append(Ei)
            S.append(Si)
        D = []
        for i in range(N):
            D.append(tuple(map(float, raw_input().split())))
        UV = []
        for i in range(Q):
            UV.append(map(int, raw_input().split()))

        sol = solve_small(N, tuple(E), tuple(S), tuple(D))
        print 'Case #{}: {}'.format(t, sol)