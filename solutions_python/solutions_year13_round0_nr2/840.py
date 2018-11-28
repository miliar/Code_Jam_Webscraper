#!/usr/bin/env python2

import sys

debug = False

if len( sys.argv ) < 2:
  print "Missing file"
  sys.exit(1)

def load( fname ):
  with open( fname ) as fd:
    cases = int( fd.readline().strip() )
    for i in range( 1, cases + 1 ):
      n, m = tuple( fd.readline().strip().split() )
      board = []
      for row in range( int( n ) ):
        board.append( [ int(c) for c in fd.readline().strip().split() ] )
      result = solve( board )
      print "Case #%s: %s" % ( i, result )


def solve( board ):
  maxcols = {}
  if debug:
    for row in board:
      print "".join( [ str(c) for c in row ] )
  for row in board:
    maxh = max( row )
    for ic in range( 0, len( row ) ):
      c = row[ic]
      if c < maxh:
        if ic in maxcols:
          colmax = maxcols[ ic ]
        else:
          colmax = max( [ board[ ir ][ic] for ir in range( len( board ) ) ] )
          maxcols[ ic ] = colmax
        if c < colmax:
          return "NO"
  return "YES"



if __name__ == "__main__":
  load( sys.argv[1] )