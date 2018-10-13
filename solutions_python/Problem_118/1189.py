#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import array
import math

def recfull( n, of ):
    if n <= 0:
      return 1
    return ( 3 + of )*recfull( n - 2, 1 )

def calc( dig ):
    if len( dig ) == 1:
      return min( 3, dig[ 0 ] )
    if len( dig ) == 0:
      return 1 # ?

    nm = min( dig[ 0 ], 3 )

    res = max(0, (nm - 1))*recfull( len( dig ) - 2, 0 )
    
    if ( nm <= dig[ -1 ] ) and ( nm > 0 ):
      res = res + calc( dig[ 1:-1 ] )

    for i in xrange( 1, len( dig ) ):
      res += recfull( i, 0 )

    return res

def func( a ):
    sa = int( math.sqrt( a ) )
    slst = map( int, str( sa ) )
    return calc( slst )

def solve( a, b ):
    return func( b ) - func( a - 1 )

def main():
  T = int(raw_input())
  #print calc( [3, 1] )
  for i in xrange( T ):
    lst = map( int, raw_input().split(' '))
    A = lst[ 0 ]
    B = lst[ 1 ]

    print 'Case #'+str(i+1)+':', solve( A, B )

if __name__ == '__main__':
    main()
