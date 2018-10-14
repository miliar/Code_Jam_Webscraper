def solve():
    A, B, K = map(int, raw_input().split())
    return sum([1 if x & y < K else 0 for x in xrange(A) for y in xrange(B)])


def main():
    T = input()
    for i in xrange(1, T + 1):
        print 'Case #%d: %d' % (i, solve())


if __name__ == '__main__':
    main()
