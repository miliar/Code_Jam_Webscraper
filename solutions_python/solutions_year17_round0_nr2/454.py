# -*- coding: utf-8 -*-

import sys

def solve(N):
    digits = map(int,list(str(N)))
    nb_digits = len(digits)
    for p in xrange(nb_digits-1,0,-1):
        if digits[p] < digits[p-1]:
            for j in xrange(p,nb_digits):
                digits[j] = 9
            digits[p-1] -= 1
            return solve(int(''.join(map(str,digits))))
    return N



filename = sys.argv[1]
with open(filename) as f:
    n_cases = int(f.readline())
    for i in xrange(n_cases):
        N = int(f.readline())
        res = solve(N)
        print 'Case #{}: {}'.format(i+1,res)
        
