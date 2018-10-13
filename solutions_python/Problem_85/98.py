#! /usr/bin/env python
# -*- coding: UTF-8 -*-

''' A
'''

import sys, math, random

########################################################################

def solve(fc):
    T = int(fc[0])

    k = 1
    for i in range(T):
        l1 = fc[k].strip()
        l1s = l1.split(' ')
        L,t,N,C = map(lambda x:int(x), l1s[:4])
        a = map(lambda x:int(x), l1s[4:])
        
        S = [ a[j%len(a)] for j in range(N)]
        Bp = sorted([ (sum(S[:j+1])-t/2 if sum(S[:j+1])-t/2 < S[j] else S[j],j) for j in range(N) if sum(S[:j+1])-t/2 > 0])[::-1][:L]
        
        h = reduce(lambda x,y:x+y,S)*2
        if Bp:
            h -= reduce(lambda x,y:(x[0]+y[0],0),Bp)[0]
        
        print 'Case #%i: %i' % ( i+1, h )

        k += 1

########################################################################

import unittest

class UT1(unittest.TestCase):
    
    def test_1(self):
        self.assertEqual(True,True)

########################################################################

assert len(sys.argv) > 1, 'args!'
fn = sys.argv[1]
fc = open(fn).readlines()

v = '-v' in sys.argv

if '--test' in sys.argv:
    unittest.TextTestRunner(verbosity=2).run(unittest.TestLoader().loadTestsFromTestCase(UT1))
else:
    solve(fc)
