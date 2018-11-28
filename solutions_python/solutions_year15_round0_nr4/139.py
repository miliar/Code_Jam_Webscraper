# -*- coding: utf-8 -*-
import sys

def check_winner(X, R, C):
    gab = 'GABRIEL'
    ric = 'RICHARD'

    if (R * C) % X != 0 or\
       X >= 7 or\
       max(R, C) < X or\
       min(R, C) < (X-1)/2+1 or\
       X > 3 and (R * C) / X < 3:
        return ric
    else:
        return gab

if __name__ == "__main__":
    f = open(sys.argv[1], 'r')
    test_num = int(f.readline())

    for i in xrange(1, test_num+1):
        data = map(int, f.readline().split())
        ans = check_winner(data[0], data[1], data[2])
        print('Case #%i: %s' % (i, ans) )
