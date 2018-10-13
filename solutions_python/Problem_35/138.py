#! /usr/bin/python
# -*- coding:utf-8

import sys

def getm(  m , w, h ):

    ret = [[ None for i in range(w) ] for j in range(h) ]

    fdic = {}
    for y in range(h):
        for x in range(w):
            fdic[ (x,y) ] = []

    ds = ((0,-1),(-1,0),(1,0),(0,1))
    for y in range(h):
        for x in range(w):
            low  = m[y][x]
            high = m[y][x]
            ldir = (x,y)
            hdir = (x,y)
            for dx,dy in ds:
                xx,yy = x+dx, y+dy
                if 0 <= xx < w and 0 <= yy < h and low > m[yy][xx]:
                    low = m[yy][xx]
                    ldir = (xx,yy)
            fdic[ ldir  ].append( (x,y) )
            fdic[ (x,y) ].append( ldir  )
        
    def f( pos, c ):
        x,y = pos
        if not ret[y][x]:
            ret[y][x] = c
            for p in fdic[pos]:
                f( p, c )

    i = ord('a')
    for y in range(h):
        for x in range(w):
            if not ret[y][x]:
                f( (x, y), chr(i) )
                i += 1
    return ret


def main( file ):
    f = open( file )
    T = int( f.readline().strip() )
    for t in range(T):
        H,W = map( int , f.readline().strip().split() )
        m = [ map( int, f.readline().strip().split() ) for i in range( H ) ]
        print "Case #%d:" % (t + 1)
        ans = getm( m, W, H )
        print "\n".join( [ " ".join( ans[y] ) for y in range(len(ans)) ] )
        
if __name__ == '__main__': main(sys.argv[1])
