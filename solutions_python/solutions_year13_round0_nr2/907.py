#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import array

def state( game, n, m ):
    state = True

    for i in xrange( n ):
      for j in xrange( m ):
        nm = game[ i ][ j ]
        ok1 = True
        ok2 = True
        for k in xrange( n ):
          if ( game[ k ][ j ] > nm ):
            ok1 = False

        for k in xrange( m ):
          if ( game[ i ][ k ] > nm ):
            ok2 = False
        
        state = state and ( ok1 or ok2 )

    if state:
      return 'YES'
    return 'NO'

def main():
  T = int(raw_input())
  for i in xrange( T ):
    lst = map( int, raw_input().split(' '))
    N = lst[ 0 ]
    M = lst[ 1 ]

    game = {}
    for j in xrange( N ):
      mylst = raw_input().split(' ')
      game[ j ] = map( int, mylst )
    print 'Case #'+str(i+1)+':', state( game, N, M )

if __name__ == '__main__':
    main()
