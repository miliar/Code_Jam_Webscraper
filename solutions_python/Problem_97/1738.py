#!/usr/bin/env python

# Solution to the small case of Recycled numbers

import sys

def Rotate( n ):
  """ Rotate a number n to get all possible rotations """
  n = str( n )
  s = set()
  while n not in s:
    s.add( n )
    n = n[1:] + n[0]
  return( [ int(n) for n in s if n[ 0 ] != '0'] )

def GenerateAllPossibleRecycles():
  """ Return a set of all possible recycles between 1 and 1000 of course """
  possibilities = set()
  for i in range( 1001 ):
    rotations = Rotate( i )
    for r in rotations:
      if r != i:
        possibilities.add( ( min( i, r ), max( i, r ) ) )
  return possibilities

def Main():
  sys.stdin.readline() # Discard the first line
  case_number = 1
  pairs = GenerateAllPossibleRecycles()

  for line in sys.stdin:
    a, b = map( int, line.split() )
    answer = [ ( x, y ) for ( x, y ) in pairs if a <= x and y <= b ]
    print "Case #%d: %d"%( case_number, len( answer ) )
    case_number += 1
  return

Main()
