import collections
import sys

from math import *


def read_line():
    return sys.stdin.readline().rstrip( '\n' )

def read_integer( base = 10 ):
    return int( read_line(), base )

def read_integers( base = 10 ):
    return [ int( x, base ) for x in read_line().split() ]

T = read_integer()
for t in range( T ):
    print 'Case #%i:' % ( t + 1 ),
    N, K = read_integers()
    count = 1
    partitions = 1
    while K >= 2*partitions:
        partitions *= 2
    N -= partitions - 1
    K -= partitions - 1
    space = N//partitions
    remainder = N % partitions
    if K <= remainder:
        space += 1
    space -= 1
    minimum = space // 2
    print space - minimum, minimum
        
