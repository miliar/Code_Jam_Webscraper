#!/usr/bin/env python2

import sys
import pprint

if len( sys.argv ) < 2:
  print "Missing file"
  sys.exit(1)

def load( fname ):
  with open( fname ) as fd:
    cases = int( fd.readline().strip() )
    for i in range( 1, cases + 1 ):
      board = []
      for row in range( 4 ):
        board.append( fd.readline().strip() )
      #Skip empty line between boards
      fd.readline()
      result = explore( board )
      print "Case #%s: %s" % ( i, result )


def explore( board ):
  ended, res = findRows( board, True )
  if res:
    return res
  ended, res = findRows( map( "".join, zip( *board ) ), ended )
  if res:
    return res
  ended, res = findDiag( board, ended )
  if res:
    return res
  if ended:
    return "Draw"
  return "Game has not completed"

def findDiag( board, ended ):
  diag = "".join( [ board[i][i] for i in range( 4 ) ] )
  ended, res = checkRow( diag, ended )
  if res:
    return ( ended, res )
  diag = "".join( [ board[i][3-i] for i in range( 4 ) ] )
  ended, res = checkRow( diag, ended )
  if res:
    return ( ended, res )
  return ( ended, False )

def findRows( board, ended ):
  for i in range( len( board ) ):
    row = board[i]
    ended, res  = checkRow( row, ended )
    if res:
      return ( ended, res )
  return ( ended, False )

def checkRow( row, ended ):
  if row.find( "X" ) > -1:
    row = row.replace( "T", "X" )
  else:
    row = row.replace( "T", "O" )
  if row == "XXXX":
    return ( ended, "X won" )
  if row == "OOOO":
    return ( ended, "O won" )
  if ended and row.find( "." ) > -1:
    ended = False
  return ( ended, False )

if __name__ == "__main__":
  load( sys.argv[1] )