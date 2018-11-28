#!/usr/bin/env python

import sys, math
import fractions
from itertools import repeat, count, cycle, ifilter, ifilterfalse, imap, starmap, tee, izip, product, combinations, permutations
from collections import defaultdict
import re


def mapInstance( foo, istream ):
  L = int( istream.readline() )
  tree = ''
  for i in xrange(L):
    tree += istream.readline().strip()
  A = int( istream.readline() )
  animals = []
  for i in xrange(A):
    animals.append( istream.readline().split() )
  return foo( tree, animals )
  
def mapInput( foo, preproc = None, istream = sys.stdin, ostream = sys.stdout ):
  N = map( int, istream.readline().split() )[0]
  if preproc:
    for i in xrange(D):
      preproc( istream.readline().split() )
  odata = starmap( mapInstance, repeat( ( foo, istream ), N ) )
  for i, d in enumerate( odata ):
    print >>sys.stderr, "Case #%d" % ( i+1 )
    print >>ostream, "Case #%d:\n%s" % ( i+1, d )
  
  
def buildTree( s ):
  tree = re.sub( r'([\d\.]+)\s*([^\s\d\.\)])', r'\1,\2', s )
  tree = re.sub( r'(\))\s*(\()', r'\1,\2', tree )
  tree = re.sub( r'(\w+)\s*(\()', r'\1,\2', tree )
  tree = re.sub( r'([a-z]+)', r'"\1"', tree )
  return eval(tree)
  
def buildFeats( animal ):
  return set( animal[2:] )
  
def walk( tree, feats ):
  node = tree
  p = 1
  if type(node) == float:
    return node
  while True:
    w, feat, left, right = node
    p *= w
    if feat in feats:
      node = left
    else:
      node = right
      
    if type(node) != tuple:
      return node*p
  
def solve( tree, animals ):
  tree = buildTree(tree)
  animals = map( buildFeats, animals )
  probs = map( lambda x: walk(tree,x), animals )
  return '\n'.join( '%.7f' % p for p in probs )
  
def main( args ):
  mapInput( solve )

if __name__ == "__main__":
  main( sys.argv )
