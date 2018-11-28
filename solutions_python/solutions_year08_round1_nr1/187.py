def solve(v1, v2):
    v1 = sorted(v1)
    v2 = sorted(v2, reverse=True)
    return sum(x*y for x,y in zip(v1, v2))


def main(in_, out):
    N = int(in_.next())
    for i in range(N):
        in_.next()
        v1 = map(int, in_.next().split())
        v2 = map(int, in_.next().split())
        print 'Case #%d: %d' % (i+1, solve(v1, v2))

if __name__ == '__main__':
    import sys
    main(sys.stdin, sys.stdout)
