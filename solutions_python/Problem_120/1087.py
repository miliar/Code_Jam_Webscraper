from sympy import Symbol
from sympy.solvers import solve
from math import floor


N = Symbol('N')


def rings(r, t):
    A_N = 2 * N ** 2 + (2 * r - 1) * N - t
    return int(floor(max([s for s in solve(A_N) if s > 0])))


if __name__ == '__main__':
    import sys
    with open(sys.argv[1], 'w') as out:
        n = int(sys.stdin.readline())
        for i in range(1, n + 1):
            r, t = map(int, sys.stdin.readline().split())
            out.write('Case #{0}: {1}\n'.format(i, rings(r, t)))
