#!/usr/bin/env python

import math, sys

def log( msg ):
    print >>sys.stderr, msg

def intList( stream ):
    return [ int(y) for y in stream.readline().split() ]

inf = 999999999
def correct( i, v, heap ):
    global inf
    if v == heap[i][0]:
        return 0
    elif i > (len( heap )-1)/2:
        return inf
    children = [heap[i*2][0],heap[i*2+1][0]]
    if heap[i][2] == 1:
        if v == True and heap[i][1] == 1 and True in children:
            return 1
        elif v == False and heap[i][1] == 0 and False in children:
            return 1
        elif v == True:
            return heap[i][1] + min( correct( i*2, True, heap ), correct( i*2+1, True, heap ) )
        elif v == False:
            return (1-heap[i][1]) + min( correct( i*2, False, heap ), correct( i*2+1, False, heap ) )
    else:
        if v == True and heap[i][1] == 1:
            return correct( i*2, True, heap ) + correct( i*2+1, True, heap )
        elif v == True and heap[i][1] == 0:
            return min( correct( i*2, True, heap ), correct( i*2+1, True, heap ) )
        elif v == False and heap[i][1] == 1:
            return min( correct( i*2, False, heap ), correct( i*2+1, False, heap ) )
        if v == False and heap[i][1] == 0:
            return correct( i*2, False, heap ) + correct( i*2+1, False, heap )
        
def solve( m, v, heap ):
    global inf
    i = (m-1)/2
    while i > 0:
        left = heap[i*2][0]
        right = heap[i*2+1][0]
        if heap[i][1] == 1:
            heap[i][0] = left and right
        else:
            heap[i][0] = left or right
        i -= 1

    n = correct( 1, v, heap )
    if n >= inf:
        return "IMPOSSIBLE"
    else:
        return str(n)



stream = sys.stdin
N = int( stream.readline() )
log( "%d test cases" % N )
bool = [ False, True ]
for i in range( N ):
    m, v = intList( stream )
    heap = [ [bool[v]] ]
    for j in range( (m-1)/2 ):
        g, c = intList( stream )
        heap.append( [ None, g, c ] )
    for j in range( (m+1)/2 ):
        l = intList( stream )[0]
        heap.append( [bool[l]] )
    print "Case #%d: %s" % ( i+1, solve( m, v, heap ) )
