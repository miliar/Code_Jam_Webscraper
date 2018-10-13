#!/usr/bin/env python

import sys

def read_line():
    return sys.stdin.readline().rstrip( '\n' )

def read_integer():
    return int( read_line() )

def read_integers():
    return [ int( x ) for x in read_line().split() ]

def read_string():
    return read_line().strip()

def read_strings():
    return read_line().split()

def input_string_stack():
    data = []
    for line in sys.stdin.readlines():
        data.extend( line.split() )
    data.reverse()
    return data

def input_integer_stack():
    return [ int( x ) for x in read_string_stack() ]

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
    print 'Case #%i:' % ( t + 1 )
    results = []
    N = read_integer()
    for n in range( N ):
        results.append( [ c for c in read_string() ] )
    victories = [ sum( [ 1.0 for c in row if c == '1' ] ) for row in results ] 
    #print victories
    games = [ sum( [ 1.0 for c in row if c != '.' ] ) for row in results ]
    #print games
    WP = [ v/g for v, g in zip( victories, games ) ]
    OWP = []
    for primary_index, row in enumerate( results ):
        total = 0.0
        count = 0.0
        for secondary_index in range( N ):
            if row[ secondary_index ] == '0':
                total += ( victories[ secondary_index ] - 1 )/( games[ secondary_index ] - 1 )
                count += 1.0
            elif row[ secondary_index ] == '1':
                total += ( victories[ secondary_index ] )/( games[ secondary_index ] - 1 )
                count += 1.0
        OWP.append( total/count )
    OOWP = []
    for primary_index, row in enumerate( results ):
        OWP_list = [ OWP[ secondary_index ] for secondary_index, game in enumerate( row ) if game != '.' ]
        OOWP.append( sum( OWP_list )/len( OWP_list ) )
    for WP_i, OWP_i, OOWP_i in zip( WP, OWP, OOWP ):
        print 0.25*WP_i + 0.50*OWP_i + 0.25*OOWP_i

