#!/usr/bin/env python

import sys

def read_line():
    return sys.stdin.readline().rstrip( '\n' )

def read_integer():
    return int( read_line() )

def read_integers():
    return [ int( x ) for x in read_line().split() ]

class memoized( object ):
   def __init__( self, function ):
      self.function = function
      self.cache = {}
   def __call__( self, *arguments ):
      try:
         return self.cache[ arguments ]
      except KeyError:
         value = self.function( *arguments )
         self.cache[ arguments ] = value
         return value

T = read_integer()
for t in range( T ):
    N, P_D, P_G = read_integers()
    if ( P_D < 100 and P_G == 100 ) or ( P_D > 0 and P_G == 0 ) or ( P_D > 0 and N == 0 ):
        possible = False
    else: 
        if N >= 100:
            possible = True
        elif P_D == 0:
            possible = True
        else:
            possible = False
            for n in range( 1, N + 1 ):
                if P_D*n% 100 == 0:
                    possible = True
                    break      
    print 'Case #%i:' % ( t + 1 ), 'Possible' if possible else 'Broken'

