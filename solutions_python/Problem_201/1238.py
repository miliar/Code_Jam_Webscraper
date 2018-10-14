#!/usr/bin/env python3
# coding=utf-8


def _div2(n):
    if n <= 0:
        return 0, 0
    if n % 2 == 0:
        return int(n / 2), int(n / 2)
    else:
        return int(n / 2) + 1, int(n / 2)


def dist(n, k):
    kb = "{0:b}".format(k)
    d = n

    for i in range(len(kb)-1, 0, -1):
        x, y = _div2(d - 1)
        if kb[i] == '0':
            d = x
        else:
            d = y

    return _div2(d - 1)


def dist2(n, k):
    d = n - k

    while k > 1:
        x, y = _div2(d)
        if k % 2 == 0:
            d = x
            k = int(k / 2)
        else:
            d = y
            k = int(k / 2) - 1

    return _div2(d)


if __name__ == '__main__':
    file = 'C-small-2-attempt0'
    with open(file + '.in', 'r') as inp:
        lines = inp.readlines()

    T = int(lines[0])
    with open(file + '.out', 'w') as out:
        for i in range(1, T + 1):
            n, k = lines[i].split(' ')
            k = int(k)
            n = int(n)
            res = dist(n, k)
            out.write('Case #%d: %d %d\n' % (i, res[0], res[1]))
