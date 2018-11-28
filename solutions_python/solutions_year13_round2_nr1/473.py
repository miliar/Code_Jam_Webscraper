#!/usr/bin/env python

import sys
import time
import logging

if len( sys.argv ) < 2:
  print( "Missing file" )
  sys.exit(1)

log = logging.getLogger( __name__ )
log.addHandler( logging.StreamHandler() )
if '-d' in sys.argv:
  log.setLevel( logging.DEBUG )
else:
  log.setLevel( logging.CRITICAL )


def load( fname ):
  with open( fname ) as fd:
    cases = int( fd.readline().strip() )
    for i in range( 1, cases + 1 ):
      log.debug( "Doing case #{0}".format( i ) )
      size = int( tuple( fd.readline().strip().split() )[0] )
      motes = list( sorted( [ int( m.strip() ) for m in fd.readline().split() if m.strip() ] ) )
      log.debug( "{0} -> {1}".format( size, motes ) )
      result = solve( size, motes )
      print( "Case #{0}: {1}".format( i, result ) )

def solve( size, motes ):
  c = 0
  for iP in range( len( motes ) ):
    m = motes[iP]
    #Normal case
    if size > m:
      size += m
      continue
    grow = size - 1
    #I can grow one
    if size + grow > m:
      size += grow + m
      c += 1
      continue
    left = len( motes ) - iP
    if grow == 0:
      return c + left
    gt = 1
    ns = size + grow
    while ns < m:
      ns += ns - 1
      gt += 1
    if left < gt:
      return c + left
    nc = solve( ns, motes[iP:] )
    return c + min( nc + gt, left )
  return c


if __name__ == "__main__":
  load( sys.argv[1] )