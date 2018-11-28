# -*- coding: utf-8 -*-
import sys
import math

def calc_opt_score(R, C, W):
    return ((C-1) / W + W)*R

if __name__ == "__main__":
    f = open(sys.argv[1], 'r')
    test_num = int(f.readline())

    for i in xrange(1, test_num+1):
        date = map(int, f.readline().split())
        ans = calc_opt_score(date[0], date[1], date[2])
        print('Case #%i: %s' % (i, ans) )
