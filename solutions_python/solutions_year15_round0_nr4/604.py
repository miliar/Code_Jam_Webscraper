# -*- coding: utf-8 -*-
from sys import stdin, stdout
from copy import copy


stdin = open('D-small-attempt0.in', 'r')
stdout = open('D-small-attempt0.out', 'w')


def solve():
    X, R, C = [int(item) for item in stdin.readline().split()]
    R, C = min(R, C), max(R, C)
    flag = False
    if not R*C % X == 0:
        flag = False
    else:
        if X == 1 or X == 2:
            flag = True
        elif X == 3:
            if R == 1:
                flag = False
            else:
                flag = True
        elif X == 4:
            if R <= 2:
                flag = False
            else:
                flag = True
    if flag:
        stdout.write('GABRIEL\n')
    else:
        stdout.write('RICHARD\n')

T = int(stdin.readline())
for t in range(T):
    stdout.write('Case #%d: ' % (t+1))
    solve()