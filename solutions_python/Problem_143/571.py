def solve(test_number):
    res = 0
    a, b, k = map(int, raw_input().split())
    for i in xrange(a):
        for j in xrange(b):
            if (i & j) < k:
                res += 1
    print 'Case #%d: %d' % (test_number, res)


def main():
    test_count = int(raw_input())
    for test_number in xrange(1, test_count + 1):
        solve(test_number)


if __name__ == '__main__':
    main()