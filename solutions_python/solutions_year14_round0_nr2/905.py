#! /usr/bin/env python

def solve(c, f, x):
    def time(nfacs, goal):
        rate = 2.0 + nfacs * f
        return goal / rate

    acc = 0.0
    nfacs = 0
    while True:
        nomore = time(nfacs, x)
        # print '%d = (%s+%s)' % (nfacs, acc, nomore)
        if x < c:
            return acc + nomore

        onefac = time(nfacs, c)
        onemore = onefac + time(nfacs + 1, x)

        if nomore < onemore:
            return acc + nomore

        acc += onefac
        nfacs += 1


def main():
    t = input()
    for i in xrange(1, t + 1):
        c, f, x = map(float, raw_input().split())
        print 'Case #{0}: {1}'.format(i, solve(c, f, x))


if __name__ == '__main__':
    main()
