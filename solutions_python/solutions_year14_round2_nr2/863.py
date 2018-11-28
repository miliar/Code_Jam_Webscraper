# -*- coding: utf-8 -*-

from sys import stdin
import numpy as np


T = int(stdin.next())
for t in xrange(T):
    A,B,K = np.fromstring(stdin.next(),int,3,' ')
    a = np.arange(A)
    b = np.arange(B)
    cnts = np.count_nonzero((b[:,None]&a[None,:])<K)
    print 'Case #%d: %d' % (t+1,cnts)
    
