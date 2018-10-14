#!/usr/bin/env python
import sys
import copy

def pdb():
  import pdb as pdb_
  pdb_.Pdb().set_trace( sys._getframe( 1 ) )

with open( sys.argv[ 1 ], "r" ) as fi:
  input = fi.read().splitlines()
fo = open( "output", "w" )

T = int( input.pop( 0 ) )
print "T:", T

for t in range( 1, T+1 ):  
  N = int( input.pop( 0 ) )
  print "t:", t, "N:", N
  words = []
  for _ in range( N ):
    words.append( input.pop( 0 ) )
  print "words:", words

  minMoves = 10000
  for i in range( N ):
    word = words[ i ]
    maxMoves = -1
    for j in range( N ):
      if j == i:
        continue
      word2 = words[ j ]
      k = 0
      m = 0
      moves = 0
      while( True ):
        if k < len( word ) and m < len( word2 ) and word[ k ] == word2[ m ]:
          k += 1
          m += 1
        elif k >= len( word ):
          if word[ k - 1 ] == word2[ m ]:
            moves += 1
            m +=1
          else:
            moves = -1
        elif m >= len( word2 ):
          if word2[ m - 1 ] == word[ k ]:
            moves += 1
            k += 1
          else:
            moves = -1
        elif k > 0 and word[ k - 1 ] == word[ k ] and word[ k ] != word2[ m ]:
          moves += 1
          k += 1
        elif m > 0 and word2[ m - 1 ] == word2[ m ] and word[ k ] != word2[ m ]:
          moves += 1
          m += 1
        else:
          moves = -1
        if moves == -1 or ( k >= len( word ) and m >= len( word2 ) ):
          break
      print "moves:", moves, "maxMoves:", maxMoves, "minMoves:", minMoves
      if moves > maxMoves:
        maxMoves = moves

    if maxMoves >= 0 and ( maxMoves < minMoves or minMoves == 10000 ):
      minMoves = maxMoves
  print "minMoves:", minMoves
  fo.write( "Case #%d: " %t )
  if minMoves != 10000:
    fo.write( "%d\n" % minMoves )
  else:
    fo.write( "Fegla Won\n" )

