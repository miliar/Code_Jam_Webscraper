#!python
#-*- coding:utf-8 -*-

import sys

T = int( sys.stdin.readline() )
for i in range(T):
    ri1 = int( sys.stdin.readline() )
    r1  = [ [ int(x) for x in sys.stdin.readline().split() ] for y in range(4) ]
    ri2 = int( sys.stdin.readline() )
    r2  = [ [ int(x) for x in sys.stdin.readline().split() ] for y in range(4) ]
    
    rc1 = set( r1[ri1 - 1] )
    rc2 = set( r2[ri2 - 1] )
    c   = rc1 & rc2
    
    if len(c) == 1:
        print "Case #%d: %d" % ( i + 1, c.pop() )
    elif len(c) == 0:
        print "Case #%d: Volunteer cheated!" % ( i + 1 )
    else:
        print "Case #%d: Bad magician!" % ( i + 1 )
