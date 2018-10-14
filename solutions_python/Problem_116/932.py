#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import array

def state( game ):
    xgame = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
    ogame = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
    xscore = []
    oscore = []

    full = False

    for i in xrange( 4 ):
      for j in xrange( 4 ):
        if (game[i][j] == 'X') or (game[i][j] == 'T'):
          xgame[i][j] = 1
        if (game[i][j] == 'O') or (game[i][j] == 'T'):
          ogame[i][j] = 1
        if (game[i][j] == '.'):
          full = True

    xcl1 = 0
    xcl2 = 0
    xcl3 = 0
    xcl4 = 0
    xd1 = 0
    xd2 = 0

    ocl1 = 0
    ocl2 = 0
    ocl3 = 0
    ocl4 = 0
    od1 = 0
    od2 = 0


    for i in xrange( 4 ):
      xscore.insert( 0, sum( xgame[ i ] ) )
      oscore.insert( 0, sum( ogame[ i ] ) )
      xcl1 += xgame[ i ][ 0 ]
      xcl2 += xgame[ i ][ 1 ]
      xcl3 += xgame[ i ][ 2 ]
      xcl4 += xgame[ i ][ 3 ]
      xd1 += xgame[ i ][ i ]
      xd2 += xgame[ i ][ 3 - i ]
      ocl1 += ogame[ i ][ 0 ]
      ocl2 += ogame[ i ][ 1 ]
      ocl3 += ogame[ i ][ 2 ]
      ocl4 += ogame[ i ][ 3 ]
      od1 += ogame[ i ][ i ]
      od2 += ogame[ i ][ 3 - i ]

    #print ogame
    xmscore = max( max( xscore ), max( xcl1, xcl2, xcl3, xcl4, xd1, xd2 ) )
    omscore = max( max( oscore ), max( ocl1, ocl2, ocl3, ocl4, od1, od2 ) )

#    print xmscore, omscore
    if xmscore == 4:
      return 'X won'
    if omscore == 4:
      return 'O won'

    if (full):
      return 'Game has not completed'

    return 'Draw'

def main():
  T = int(raw_input())
  for i in xrange( T ):
    game = [[], [], [], []]
    for j in xrange( 4 ):
      game[ j ] = list( raw_input() )
    print 'Case #'+str(i+1)+':', state( game )
    raw_input()

if __name__ == '__main__':
    main()
