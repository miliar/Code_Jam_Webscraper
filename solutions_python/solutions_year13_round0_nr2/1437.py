#!/usr/bin/env python

from numpy import *

def inputs():
    return tuple(map(int, raw_input().split(' ')))

(T,) = inputs()
for t in range(T):
    print "Case #%d:" % (t+1,),
    lawn = empty(inputs(), dtype=int)
    for i in range(lawn.shape[0]):
        lawn[i, :] = inputs()
    h_x = lawn.max(axis=0, keepdims=True)
    h_y = lawn.max(axis=1, keepdims=True)
    if (lawn == minimum(h_x, h_y)).all():
        print 'YES'
    else:
        print 'NO'
    
