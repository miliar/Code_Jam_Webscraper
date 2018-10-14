import numpy as np
import math

#------------------------------------
# Read inputs
t = int(raw_input())
for i in xrange(1, t + 1):
    D,N = (int(s) for s in raw_input().split(" "))
    K = []
    S = []
    tm= []
    for j in xrange(0,N):
        t1,t2 = (int(s) for s in raw_input().split(" "))
        K.append(t1)
        S.append(t2)
        tm.append(float(D-t1)/float(t2))

    print "Case #{}:".format(i) ,
    print '%.14f' % (D/max(tm))
