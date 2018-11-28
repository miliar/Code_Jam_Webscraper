#!/usr/bin/env python

import sys, math
import fractions
from itertools import repeat, count, cycle, ifilter, ifilterfalse, imap, starmap, tee, izip, product, combinations, permutations
from collections import defaultdict


def mapInstance( foo, istream ):
  N = istream.readline().strip()
  return foo( N )
  
def mapInput( foo, preproc = None, istream = sys.stdin, ostream = sys.stdout ):
  N = map( int, istream.readline().split() )[0]
  if preproc:
    for i in xrange(D):
      preproc( istream.readline().split() )
  odata = starmap( mapInstance, repeat( ( foo, istream ), N ) )
  for i, d in enumerate( odata ):
    print >>sys.stderr, "Case #%d" % ( i+1 )
    print >>ostream, "Case #%d: %s" % ( i+1, d )
  
  
def solve( N ):
  N = map(int,N)
  
  currMax = N[-1]
  for i in count(2):
    if i > len(N):
      N.sort()
      N.insert(1, 0)
      if N[0] == 0:
        for i in range(2,len(N)):
          if N[i] != 0:
            N[0] = N[i]
            N[i] = 0
            break
      return ''.join( map( str, N ) )
    elif N[-i] >= currMax:
      currMax = N[-i]
    else:
      el = N[-i]
      larger = filter( lambda x: x > el, N[-i+1:] )
      repl = min(larger)
      N[-i] = repl
      N[ N.index( repl, -i+1 ) ] = el
      N = N[:-i+1] + sorted( N[-i+1:] )
      return ''.join( map( str, N ) )
  
  
def main( args ):
  mapInput( solve )

if __name__ == "__main__":
  main( sys.argv )
