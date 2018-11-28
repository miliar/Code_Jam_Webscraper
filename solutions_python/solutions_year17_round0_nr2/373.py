#!/usr/bin/python2
# -*- coding: utf-8 -*-
# †
def f(x):
    a = map(int, str(x))
    n = len(a)
    # i桁め, 最大の桁の数字はd, i桁めまでの値, 答え未満の値かどうか
    def rec(i, d, summ, smaller):
        if i == n:
            return summ
        maxi = 0
        if smaller:
            maxi = max(maxi, rec(i+1, 9, summ*10 + 9, smaller))
        # a[i] にしたい。できるのは d <= a[i] のとき
        if d <= a[i]:
            maxi = max(maxi, rec(i+1, a[i], summ*10 + a[i], smaller))
        # a[i]-1 にしたい。できるのは d <= a[i]-1 のとき
        if d <= a[i] - 1:
            maxi = max(maxi, rec(i+1, a[i]-1, summ*10 + a[i]-1, True))
        return maxi

    res = rec(0, 0, 0, False)
    return res


T = int(raw_input())
for loop in xrange(T):
    x = int(raw_input())
    res = f(x)
    print 'Case #{}: {}'.format(loop+1, res)
