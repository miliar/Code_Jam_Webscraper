#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys

def output(can_win):
    if can_win:
        return 'GABRIEL'
    else:
        return 'RICHARD'

def solve(X, R, C):
    if X <= 2:
        return output(R*C % X ==0)
    elif X ==3:
        return output(R*C % X == 0 and R >= 2 and C >=2)
    else :
        return output(R*C % X == 0 and R >= 3 and C >=3)


if __name__ == "__main__":
    T = input()
    for t in xrange(1, T+1):
        X, R, C = map(int ,sys.stdin.readline().split())
        print "Case #{no}: {result}".format(no=t, result=solve(X, R, C))