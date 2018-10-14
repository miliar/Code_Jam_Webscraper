#!/usr/bin/env python3


def div(a, b):
    return not a % b


def gabe_win(X, R, C):
    large = R > X-2 and C > X-2
    return div(R*C, X) and large


def solution(*args):
    if gabe_win(*args):
        return 'GABRIEL'
    else:
        return 'RICHARD'


if __name__ == '__main__':
    for i in range(int(input())):
        print('Case #{}: {}'.format(i+1, solution(*map(int, input().split()))))
