import fileinput
from itertools import product, ifilter


def solve(A, B, K):
    prod = product(xrange(A), xrange(B))
    wins = ifilter(lambda (a, b): (a & b) < K, prod)
    return len(list(wins))


def run():
    f = fileinput.input()
    T = int(f.readline())
    for t in xrange(1, T + 1):
        A, B, K = map(int, f.readline().split(' '))
        print 'Case #%d: %d' % (t, solve(A, B, K))


if __name__ == '__main__':
    run()