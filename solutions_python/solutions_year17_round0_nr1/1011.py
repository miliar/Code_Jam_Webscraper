#!/usr/bin/env python
# pylint:disable=missing-docstring,invalid-name


def booleanize(s):
    return [item == '+' for item in s]


def flip(s, p, k):
    for i in range(p, p + k):
        s[i] = not s[i]


def main():
    rs = int(raw_input())
    for rn in range(rs):
        print 'Case #%d: ' % (rn + 1),

        line = raw_input().strip().split()
        s = booleanize(line[0])
        k = int(line[1])
        l = len(s)

        tot = 0
        for p in range(l - k + 1):
            if not s[p]:
                flip(s, p, k)
                tot += 1

        for p in range(l - k + 1, l):
            if not s[p]:
                print 'IMPOSSIBLE'
                break
        else:
            print tot


if __name__ == '__main__':
    main()
