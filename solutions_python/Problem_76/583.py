#! /usr/bin/python2.6
# coding: utf-8
import itertools

def sumxor(lst):
    return reduce(lambda x,y:x^y, lst, 0)

def seanmax(target):
    if len(target) == 2 and target[0] == target[1]:
        return target[0]
    ret = -1
    for i in range(len(target) / 2):
        for n in itertools.combinations(target, i + 1):
            lst1 = n
            lst2 = [x for x in target if not (x in n)]
            xa, xb = sumxor(lst1), sumxor(lst2)
            aa, ab = sum(lst1), sum(lst2)
            if xa == xb:
                ret = max(ret, max(aa, ab))
    return ret


# is it possible?
# sean's pile
ntcases = int(raw_input())

for tcase in range(1, ntcases+1):
    N = int(raw_input())
    lst = map(int, raw_input().split())
    n = seanmax(lst)
    print 'Case #%d: %s' % (tcase, n if n > -1 else 'NO')
