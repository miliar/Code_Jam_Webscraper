#!/usr/bin/python2.7
import sys


def move_exists(x, r, c):
    if (r * c) % x:
        return True
    if (x + 1) / 2 > min(r, c):
        return True
    if x > max(r, c):
        return True
    if r > c:
        r, c = c, r
    if x == 4:
        if r == 2 and c <= 4:
            return True
    return False


def get_res(x, r, c):
    return 'RICHARD' if move_exists(x, r, c) else 'GABRIEL'


if __name__ == "__main__":
    tcn = int(sys.stdin.readline())
    for tc in range(tcn):
        x, r, c = map(int, sys.stdin.readline().split())
        print 'Case #%d:' % (tc + 1,), get_res(x, r, c)
