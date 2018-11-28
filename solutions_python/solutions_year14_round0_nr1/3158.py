#!/usr/bin/env python


def read_values():
    r = int(raw_input()) - 1
    for i in xrange(4):
        line = raw_input()
        if i == r:
            v = set(map(int, line.split()))
    return v


def main():
    n_tests = int(raw_input())
    for test in xrange(1, n_tests + 1):
        v = read_values() & read_values()
        if not v:
            s = 'Volunteer cheated!'
        elif len(v) > 1:
            s = 'Bad magician!'
        else:
            s = next(iter(v))
        print 'Case #{}: {}'.format(test, s)


if __name__ == '__main__':
    main()
