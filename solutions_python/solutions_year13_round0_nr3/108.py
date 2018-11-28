#!/usr/bin/env python

import sys
from itertools import combinations

t = int(sys.stdin.readline())

def is_palindrome(x):
    return str(x) == ''.join(reversed(str(x)))

#   fairsquares = list()
#   for num in xrange(9999,0,-1):
    #   pal = int(str(num) + ''.join(reversed(str(num))))
    #   cand = pal * pal
    #   if is_palindrome(cand):
        #   fairsquares.append(cand)
    #   pal = int(str(num) + ''.join(reversed(str(num)[:-1])))
    #   cand = pal * pal
    #   if is_palindrome(cand):
        #   fairsquares.append(cand)

def make_roots():
    roots = [1,2,3]
    for n1 in xrange(1,5):
        for comb in combinations(xrange(25),n1):
            num = ''.join('1' if i in comb else '0' for i in xrange(25))
            num = str(int(num))   #drops prepended 0's
            roots.append(int(num + ''.join(reversed(num))))
            roots.append(int(num + '1' + ''.join(reversed(num))))
            roots.append(int(num + '0' + ''.join(reversed(num))))

    for i in xrange(50):
        roots.append(int('2' + '0'*i + '2'))

    for i in xrange(25):
        roots.append(int('2' + '0'*i + '1' + '0'*i + '2'))

    for i in xrange(25):
        s = '1' + '0'*i + '2' + '0'*i + '1'
        roots.append(int(s))
        for j in xrange(i):
            s = list('1' + '0'*i + '2' + '0'*i + '1')
            s[j+1] = '1'
            s[len(s) - j - 2] = '1'
            roots.append(int(''.join(s)))

    return roots

fairsquares = [r*r for r in make_roots()] # if r*r < 1e14]

for testcase in xrange(t):
    [a,b] = map(int,sys.stdin.readline().split())
    print 'Case #' + str(testcase+1) + ': ' + str(sum(a<=fs<=b for fs in fairsquares))





