#!/usr/bin/python
# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <codecell>

import difflib
import numpy as np
# <codecell>

with open('B-small-attempt0.in') as fIn:
    n_case = int(fIn.readline())
    for case in range(n_case):
        [a,b,k] = fIn.readline().split()
        a = int(a)
        b = int(b)
        k = int(k)
        #print '============',a,b,k,'============='
        mgrid = np.zeros((a,b))
        for i in range(a):
            for j in range(b):
                mgrid[i,j] = i&j
        #print (mgrid < k).sum()
        
        
        print 'Case #{0}:'.format(case+1), (mgrid < k).sum()

# <codecell>


