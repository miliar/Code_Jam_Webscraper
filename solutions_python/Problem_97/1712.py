#!/usr/bin/env python 
######################################################################
## Filename:    A.py
## Version:     $Revision: 1.0 $
## Description: 
## Creator:     Rui Pereira <rui.pereira@in2p3.fr>
## Created:     14-04-2012 18:06:30
## Modified:    Time-stamp: <2012-04-14 19:56:55 rui>
## CVS info:    $Id: A.py, v 1.0 14-04-2012 18:06:30 pereira Exp $
######################################################################
"""
"""

__author__ = 'Rui Pereira <rui.pereira@in2p3.fr>'
__version__ = '$Revision$'

import sys
import math

inv2 = lambda i,a: int(i[a:] + i[:a])
inv = lambda i,j,k: [inv2(i,a) for a in range(len(i))
                     if j <= inv2(i,a) <= k]
nc = lambda i,j : math.factorial(i)/(math.factorial(j)*math.factorial(i-j))

def compute(i,j):
    N = range(i, j)
    t = 0
    done = []
    for i in [inv(str(n),i,j) for n in N]:
        if len(set(i)) > 1 and i[0] not in done:
            done.extend(i)
            t += nc(len(set(i)), 2)
    return t

for n,l in enumerate(open(sys.argv[1]).read().splitlines()[1:]):
    print 'Case #%i: %s' % (n+1, compute(*map(int, l.strip().split())))
