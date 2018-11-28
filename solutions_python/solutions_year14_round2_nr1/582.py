import itertools


def solve():
    n = input()
    strings = [raw_input().strip() for i in xrange(n)]
    grouped = [[k for k, g in itertools.groupby(s)] for s in strings]
    nums = [[sum([1 for item in g]) for k, g in itertools.groupby(s)]
            for s in strings]
    same = reduce(lambda x, y: (y, x[0] == y and x[1]),
                  grouped,
                  (grouped[0], True))
    if not same[1]:
        return False
    nums_t = zip(*nums)
    average = [int(round(float(sum(x)) / len(x))) for x in nums_t]
    steps = sum(itertools.imap(
        lambda x, y: sum([abs(i - y) for i in x]), nums_t, average))
    return steps


def main():
    T = input()
    for i in xrange(1, T + 1):
        num = solve()
        print 'Case #%d:' % i,
        if num is False:
            print 'Fegla Won'
        else:
            print num


if __name__ == '__main__':
    main()
