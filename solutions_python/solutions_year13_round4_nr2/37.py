import sys


def compute(N, P):
    b = bin(P - 1)[2:]
    if len(b) < N:
        A = 0
    elif '0' not in b:
        A = 2 ** N - 1
    else:
        i = b.index('0') + 1
        A = 2 ** i - 2
    if P == 1:
        B = 0
    elif len(b) == N and '0' not in b:
        B = 2 ** N - 1
    elif '0' not in b:
        i = N - len(b)
        B = 2 ** N - 2 ** i
    else:
        i = N - len(b) + 1
        B = 2 ** N - 2 ** i
    return "%s %s" % (A, B)


def parse():
    N, P = map(int, sys.stdin.readline().strip().split())
    return N, P


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
