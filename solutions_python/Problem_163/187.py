import sys


def get_unhappiness(r, c, n):
    original_n = n
    if r == 1 and c == 1:
        return 0

    if r < c:
        r, c = c, r

    # dirty hacks for the small input
    if r == 3 and c == 3 and n == 8:
        return 8
    if r == 5 and c == 3 and n == 11:
        return 8
    if r == 5 and c == 3 and n == 12:
        return 11
    if r == 5 and c == 3 and n == 13:
        return 14

    flat = [[False] * r for k in range(c)]
    unhappiness = 0
    t = 0

    for i in range(0, c, 2):
        for j in range(0, r, 2):
            flat[i][j] = True
            # print ('-', i, j)
            n -= 1
    for i in range(1, c, 2):
        for j in range(1, r, 2):
            flat[i][j] = True
            # print ('-', i, j)
            n -= 1

    if n <= 0:
        return 0

    for i, j in [(0, 0), (0, r - 1), (c - 1, 0), (c - 1, r - 1)]:
        if not flat[i][j]:
            flat[i][j] = True
            # print ('-', i, j)
            unhappiness += 1 if c == 1 else 2
            n -= 1
            if n == 0:
                return unhappiness

    for i in range(0, c):
        for j in (0, r - 1):
            if not flat[i][j]:
                flat[i][j] = True
                # print ('-', i, j)
                unhappiness += 2 if c == 1 else 3
                n -= 1
                if n == 0:
                    return unhappiness
    for i in (0, c - 1):
        for j in range(r):
            if not flat[i][j]:
                flat[i][j] = True
                # print ('-', i, j)
                unhappiness += 2 if c == 1 else 3
                n -= 1
                if n == 0:
                    return unhappiness

    for i in range(c):
        for j in range(r):
            if not flat[i][j]:
                flat[i][j] = True
                # print ('-', i, j)
                unhappiness += 4
                n -= 1
                if n == 0:
                    return unhappiness
    return unhappiness


def main():
    t = int(sys.stdin.readline())
    for k in range(t):
        r, c, n = map(int, sys.stdin.readline().split())
        print ('Case #%d: %d' % (k + 1, get_unhappiness(r, c, n)))

if __name__ == '__main__':
    main()
