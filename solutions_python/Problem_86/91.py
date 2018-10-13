#! /usr/bin/env python
# -*- coding: UTF-8 -*-

''' C
'''

import sys, math, random

########################################################################

def solve(fc):
    T = int(fc[0])

    k = 1
    for i in range(T):
        l1 = fc[k].strip()
        # the number of other players, the lowest and the highest note Jeff's instrument can play
        N,L,H = map(lambda x:int(x), l1.split(' '))
        k += 1
        ns = map(lambda x:int(x), fc[k].split(' '))
        
        note = -1
        for j in range(L,H+1):
            harmony = True
            for n in ns:
                if not (n%j==0 or j%n==0):
                    harmony = False
                    break
            if harmony:
                note = j
                break
        
        if harmony and note >= 0:
            print 'Case #%i: %i'%(i+1,note)
        else:
            print 'Case #%i: NO'%(i+1)
        
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
