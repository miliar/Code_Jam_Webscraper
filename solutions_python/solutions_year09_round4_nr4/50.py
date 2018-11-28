#!/usr/bin/env python

import sys, math
import fractions
from itertools import repeat, count, cycle, ifilter, ifilterfalse, imap, starmap, tee, izip, product, combinations, permutations
from collections import defaultdict
from operator import itemgetter


def mapInstance( foo, istream ):
  N = int( istream.readline() )
  idata = []
  for i in xrange(N):
    idata.append( map( int, istream.readline().split() ) )
  return foo( idata )
  
def mapInput( foo, preproc = None, istream = sys.stdin, ostream = sys.stdout ):
  N = map( int, istream.readline().split() )[0]
  if preproc:
    for i in xrange(D):
      preproc( istream.readline().split() )
  odata = starmap( mapInstance, repeat( ( foo, istream ), N ) )
  for i, d in enumerate( odata ):
    print >>sys.stderr, "Case #%d" % ( i+1 )
    print >>ostream, "Case #%d: %s" % ( i+1, d )
  
class showfunction:
  def __init__( self, foo ):
    self.foo = foo
    
  def __call__( self, *args ):
    result = self.foo( *args )
    print >>sys.stderr, args, result
    return result

class cachedfunction:
  def __init__( self, foo ):
    self.foo = foo
    self.cache = {}
    
  def __call__( self, *args ):
    if args in self.cache:
      return self.cache[args]
    else:
      result = self.cache[args] = self.foo( *args )
      return result

def solve( idata ):
  if len(idata) <= 2:
    return "%.6f" % max(map(itemgetter(2),idata))
  elif len(idata) == 3:
    m = 100000
    for i in xrange(len(idata)):
      for j in xrange(i+1,len(idata)):
        r = math.hypot(idata[i][0]-idata[j][0], idata[i][1]-idata[j][1]) + idata[i][2] + idata[j][2]
        m = min(r,m)
    return "%.6f" % (m/2.0)
  else:
    def foo(*args):
      a = -1
      b = -1
      for i in xrange(len(args)):
        for j in xrange(i+1, len(args)):
          if args[i] != args[j]: continue
          r = math.hypot(idata[i][0]-idata[j][0], idata[i][1]-idata[j][1]) + idata[i][2] + idata[j][2]
          if args[i] == 0:
            a = max(r,a)
          else:
            b = max(r,b)
      return max(a,b)
    m = min(starmap( foo, product((0,1), repeat=len(idata)) ))
    return "%.6f" % (m/2.0)
  
def main( args ):
  mapInput( solve )

if __name__ == "__main__":
  main( sys.argv )
