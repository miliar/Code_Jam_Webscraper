#!/usr/bin/env python

import sys

def read_line():
    return sys.stdin.readline().rstrip( '\n' )

def read_integer():
    return int( read_line() )

def read_strings():
    return read_line().split()

T = read_integer()
for t in range( T ):
    line = read_strings()
    line.reverse()
    combinations = {}
    C = int( line.pop() )
    for c in range( C ):
        first, second, replacement = line.pop()
        combinations[ first + second ] = replacement
        combinations[ second + first ] = replacement
    oppositions = {}
    D = int( line.pop() )
    for d in range( D ):
        first, second = line.pop()
        oppositions.setdefault( first, set() ).add( second )
        oppositions.setdefault( second, set() ).add( first )
    N = int( line.pop() )
    sequence = line.pop()
    output = []
    for letter in sequence:
        while output and output[ -1 ] + letter in combinations:
            letter = combinations[ output.pop() + letter ]
        if letter in oppositions and oppositions[ letter ].intersection( output ):
            output = []
        else:
            output.append( letter )
    print 'Case #%i:' % ( t + 1 ), str( output ).replace( "'", '' )