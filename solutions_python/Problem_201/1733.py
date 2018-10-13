import sys
import math


def solve(N, K):
    M = math.floor(math.log(K, 2))
    S = ((N - K) >> M) + 1
    return S >> 1, (S - 1) >> 1


def main(fn):
    with open(fn, 'r') as fi:
        with open(fn + '.out', 'w') as fo:
            T = int(next(fi).strip())
            for t in range(1, T + 1):
                N, K = map(int, next(fi).split())
                upper, lower = solve(N, K)
                fo.write('Case #%d: %d %d\n' % (t, upper, lower))


if __name__ == '__main__':
    main(sys.argv[1])
