# -*- coding: utf-8 -*-

import math
from bisect import * 

def shelve(a, b):
    h = int(math.sqrt(a))
    if h ** 2 == a:
        mi = h
    else:
        mi = h + 1
    ma = int(math.sqrt(b))
    return [e ** 2 for e in xrange(mi, ma+1) if is_palindrome(e) and is_palindrome(e ** 2)]

def is_palindrome(n):
    if str(n) == str(n)[::-1]:
        return True
    return False

if __name__ == '__main__':
    t = int(raw_input())
    li = shelve(1, 10 ** 14)
    for i in xrange(1, t+1):
        n, m = [int(e) for e in raw_input().split(' ')]
        print 'Case #%d:' % i, (bisect(li, m) - bisect_left(li, n))

