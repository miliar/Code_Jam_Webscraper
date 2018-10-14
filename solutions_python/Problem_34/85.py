#!/usr/bin/env python

import sys, math
#import fractions
from itertools import repeat, count, cycle, ifilter, ifilterfalse, imap, starmap, tee, izip #, product, combinations, permutations
from collections import defaultdict


def mapInstance( foo, istream ):
  idata = map( str, istream.readline().split() )
  return foo( idata )
  
def mapInput( foo, preproc = None, istream = sys.stdin, ostream = sys.stdout ):
  L, D, N = map( int, istream.readline().split() )
  if preproc:
    for i in xrange(D):
      preproc( istream.readline().split() )
  odata = starmap( mapInstance, repeat( ( foo, istream ), N ) )
  for i, d in enumerate( odata ):
    print >>ostream, "Case #%d: %s" % ( i+1, d )
  
def nodeFactory():
  return [ None ] * 256
root = nodeFactory()

def addWord( word ):
  word = word[0]

  global root
  n = root
  for c in word:
    c = ord( c )
    if not n[c]:
      n[c] = nodeFactory()
    n = n[c]
    
    
def lang( data ):
  word = data[0]

  global root
  its  = [ root ]

  i = 0
  while i < len(word):
    if word[i] == '(':
      end = word.index( ')', i+1 )
      tokens = word[i+1:end]
      i = end+1
    else:
      tokens = word[i]
      i += 1

    newits = []
    for it in its:
      newits.extend( filter( None, map( it.__getitem__, map( ord, tokens ) ) ) )
    its = newits
  return str( len( its ) )


def main( args ):
  mapInput( lang, addWord )

if __name__ == "__main__":
  main( sys.argv )
