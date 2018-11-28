import sys


class Solved(Exception):
    pass


def solve(x, r, c):
    if (r * c) < x:
        raise Solved('RICHARD')

    if (r * c) % x:
        raise Solved('RICHARD')

    for a in range(1, x):
        b = x - a + 1
        if (a > r or b > c) and (a > c or b > r):
            raise Solved('RICHARD')

    if x == 4:
        if r == 2 or c == 2:
            raise Solved('RICHARD')

    raise Solved('GABRIEL')


if __name__ == '__main__':
    for i in range(int(sys.stdin.readline())):
        x, r, c= map(int, sys.stdin.readline().strip().split(' '))

        try:
            solve(x, r, c)
        except Solved as e:
            print('Case #{}: {}'.format(i+1, e))
