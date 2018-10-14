import sys


def compute(N):
    for i in xrange(len(N) - 1):
        if int(N[i]) > int(N[i + 1]):
            if N[i] == '1':
                return '9' * (len(N) - 1)
            for j in xrange(len(N)):
                if N[i] == N[j]:
                    prefix = N[:j]
                    x = str(int(N[j]) - 1)
                    return prefix + x + ('9' * (len(N) - j - 1))
    return N


def parse():
    return sys.stdin.readline().strip(),


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
