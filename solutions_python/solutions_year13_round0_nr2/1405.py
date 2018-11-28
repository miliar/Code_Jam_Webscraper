#!/usr/bin/env python3

import sys


def main():
    if len(sys.argv) < 2 or len(sys.argv) > 3:
        print('Usage: {0} IN_FILE [OUT_FILE]'.format(sys.argv[0]))
        return

    in_file = open(sys.argv[1])
    out_file = open(sys.argv[1]+'.txt' if len(sys.argv) == 2 else sys.argv[2], mode='w')
    cases = int(next(in_file))
    for c in range(cases):
        n, m = [int(x) for x in next(in_file).rstrip('\n').split(' ')]
        lawn = [[0 for j in range(m)] for i in range(n)]  # lawn[n][m]
        for i in range(n):
            line = next(in_file).rstrip('\n')
            for j, char in enumerate(line.split(' ')):
                lawn[i][j] = int(char)
        result = check_lawn(lawn, n, m)
        out_file.write('Case #{0}: {1}\n'.format(c+1, 'YES' if result else 'NO'))


def check_lawn(lawn, n, m):
    for i in range(n):
        for j in range(m):
            if not can_reach_boundary(lawn, n, m, (i, j)):
                return False

    return True


def can_reach_boundary(lawn, n, m, pos):
    i, j = pos
    val = lawn[i][j]
    if val < 1 or val > 100:
        return False

    # ->
    canxpos = True
    for x in range(j, m):
        if val < lawn[i][x]:
            canxpos = False
    # <-
    canxneg = True
    for x in range(0, j):
        if val < lawn[i][x]:
            canxneg = False

    if canxneg and canxpos:
        return True

    # ^
    canypos = True
    for x in range(i, n):
        if val < lawn[x][j]:
            canypos = False

    # v
    canyneg = True
    for x in range(0, n):
        if val < lawn[x][j]:
            canyneg = False

    if canyneg and canypos:
        return True

    return False

if __name__ == '__main__':
    main()
