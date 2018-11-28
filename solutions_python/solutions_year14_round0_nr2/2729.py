#!/usr/bin/env python


def calc(c, f, x, c0=2.0):
    i = 0

    sn = 0.0
    ai = 1.0 * c0
    xn = x / ai

    while True:
        sn += c / ai
        ai += f
        xn1 = sn + x / ai
        if xn < xn1:
            return xn
        xn = xn1
        i += 1


def task():
    return '%.7f' % calc(*map(float, raw_input().split(' ')))


def main():
    T = int(raw_input())
    for _ in xrange(T):
        print 'Case #%d: %s' % (_ + 1, task())


if __name__ == '__main__':
    main()
