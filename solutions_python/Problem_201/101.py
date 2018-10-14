import sys


def split(N):
    if N % 2 == 0:
        u = N / 2
        v = u - 1
    else:
        u = N // 2
        v = u
    return '%d %d' % (u, v)


def compute(N, K):
    a = (N, 1)
    b = (N - 1, 0)
    while True:
        if K <= a[1]:
            return split(a[0])
        if K <= a[1] + b[1]:
            return split(b[0])
        K -= a[1] + b[1]
        if a[0] % 2 == 0:
            a, b = (a[0] / 2, a[1]), (a[0] / 2 - 1, a[1] + 2 * b[1])
        else:
            a, b = (a[0] // 2, 2 * a[1] + b[1]), (a[0] // 2 - 1, b[1])


def parse():
    N, K = map(int, sys.stdin.readline().strip().split())
    return N, K


if __name__ == "__main__":
    sys.setrecursionlimit(100000)
    T = int(sys.stdin.readline().strip())
    count = 1
    part = 0
    if len(sys.argv) == 3:
        part = int(sys.argv[1])
        count = int(sys.argv[2])
    for i in xrange(T):
        data = parse()
        if i * count >= part * T and i * count < (part + 1) * T:
            result = compute(*data)
            print "Case #%d: %s" % (i + 1, result)
