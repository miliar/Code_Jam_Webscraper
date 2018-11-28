#!/usr/bin/env python3
# coding=utf-8


def flipper(pancakes, k):
    l = len(pancakes)
    pancakes = list(pancakes)
    i = 0
    f = 0
    while True:
        if i + k > l:
            for j in range(l):
                if pancakes[j] == '-':
                    return 'IMPOSSIBLE'
            return str(f)

        if pancakes[i] == '-':
            f += 1
            for j in range(k):
                if pancakes[i + j] == '-':
                    pancakes[i + j] = '+'
                else:
                    pancakes[i + j] = '-'

        i += 1
        if i == l:
            return str(f)


if __name__ == '__main__':
    file = 'A-large'
    with open(file + '.in', 'r') as inp:
        lines = inp.readlines()

    T = int(lines[0])
    with open(file + '.out', 'w') as out:
        for i in range(1, T + 1):
            pancakes, k = lines[i].split(' ')
            k = int(k)
            res = flipper(pancakes, k)
            out.write('Case #%d: %s\n' % (i, res))
