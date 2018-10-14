#!/usr/bin/env python

from collections import namedtuple
import sys
import multiprocessing

State = namedtuple( "state", [ 'dist', 'x', 'y', 'l', 'route' ] )
dirs = ( ( 'N', 0, 1 ),
         ( 'S', 0, -1 ),
         ( 'E', 1, 0 ),
         ( 'W', -1, 0 ) )

def solve( dx, dy ):
  wtf = [ State( dx+dy, 0, 0, 1, '' ) ]
  visited = set( (0,0) )

  while wtf:
    state = wtf.pop(0)
    visited.add( ( state.x, state.y ) )
    for d, ix, iy in dirs:
      nx = state.x + ix * state.l
      ny = state.y + iy * state.l
      if ( nx, ny ) in visited:
        continue
      nroute = state.route + d
      if nx == dx and ny == dy:
        return nroute
      ndist = abs ( dx - nx ) + abs ( dy - ny )
      wtf.append( State( ( ndist, state.l ) , nx, ny, state.l + 1, nroute ) )
    wtf.sort()
  return "IMPOSSIBLE"

if __name__ == '__main__':
  cases = int( sys.stdin.readline().strip() )
  pos = []
  for case in range( cases ):
    dx, dy = map( int, sys.stdin.readline().strip().split() )
    pos.append( ( case + 1, dx, dy ) )

  solutions = []

  def do( cro ):
    case, dx, dy = cro
    return ( case, solve( dx, dy ) )

  pool = multiprocessing.Pool()
  for i in pool.map( do, pos ):
    print( "Case #{0}: {1}".format( i[0], i[1] ) )
