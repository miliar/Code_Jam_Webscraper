#!/usr/bin/python

import sys

ipt = []
src = []


def read():
    return sys.stdin.readlines()

def test( row, col, tiles ):
    for i in range( row ):
        for j in range( col ):
            if tiles[i][j] == '#':
                try:
                    if tiles[i+1][j] == '#' and tiles[i][j+1] == '#' and tiles[i+1][j+1] == '#':
                           tiles[i][j] = '/'
                           tiles[i][j+1] = '\\'
                           tiles[i+1][j] = '\\'
                           tiles[i+1][j+1] = '/'
                    else:
                        return 'Impossible'
                except:
                    return 'Impossible'


    tilestr = ''
    for row in tiles:
        tilestr += ''.join( row )
        tilestr += '\n'
    return tilestr[:-1]


def runtest():
    readp = 0
    for x in range(cases):
        #TODO :implement test code
        rowandcol = ipt[ readp + 1 ].split(' ')
        row = int( rowandcol[0] )
        col = int( rowandcol[1] )
        tiles = []
        for i in range( row ):
            tiles.append( list( ipt[ readp+2+i ][:-1] ) )

        ret = test( row, col, tiles )
        readp += row + 1
        print "Case #" + str(x + 1) + ":\n" + ret

if __name__ == '__main__':
    ipt = read()
    cases = int( ipt[0] )
    runtest()



