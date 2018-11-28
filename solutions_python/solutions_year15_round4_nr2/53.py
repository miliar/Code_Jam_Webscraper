import decimal
from decimal import Decimal

def solve(X, C, V):
    V.sort(cmp=lambda x, y: cmp(x[1], y[1]))
    if len(V) == 1:
        if C != V[0][1]:
            return 'IMPOSSIBLE'
        else:
            return Decimal(X) / Decimal(V[0][0])
    elif len(V) == 2:
        if C < V[0][1] or C > V[1][1]:
            return 'IMPOSSIBLE'
        if C == V[0][1] == V[1][1]:
            return Decimal(X) / Decimal(V[0][0] + V[1][0])
        if C == V[0][1]:
            return Decimal(X) / Decimal(V[0][0])
        if C == V[1][1]:
            return Decimal(X) / Decimal(V[1][0])
        X1 = Decimal(X) * Decimal(C - V[0][1]) / Decimal(V[1][1] - V[0][1])
        X0 = Decimal(X) - X1
        ans = max(X0 / Decimal(V[0][0]), X1 / Decimal(V[1][0]))
    return ans

def main():
    T = input()
    decimal.getcontext().prec = 9
    for i in xrange(1, T + 1):
        N, X, C = raw_input().strip().split()
        N = int(N)
        X = float(X)
        C = float(C)
        V = []
        for r in xrange(N):
            v, r = map(float, raw_input().strip().split())
            V.append((v, r))
        print 'Case #{0}: {1}'.format(i, solve(X, C, V))


if __name__ == '__main__':
    main()
