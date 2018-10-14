
import sys
from functools import partial as p
from operator import *
rl = sys.stdin.readline
n = int( rl() )
for i in range( 1, n+1 ):
    print 'Case #%d: '%i,
    cont_flag = False
    m = [ rl()[:4] for j in range( 4 ) ]
    dot = reduce( add, map( methodcaller( 'count', '.' ), m ) )
    rl()
    d = m
    d += map( p( reduce, add ), zip( *m ) )
    d.append( reduce( add, [ m[x][x] for x in range( 4 ) ] ) )
    d.append( reduce( add, [ m[x][3-x] for x in range( 4 ) ] ) )
    x = map( methodcaller( 'count', 'X' ), d )
    o = map( methodcaller( 'count', 'O' ), d )
    t = map( methodcaller( 'count', 'T' ), d )
    for j in range( len( d ) ):
        if x[j] + t[j] == 4:
            print 'X won'
            cont_flag = True
            break
        if o[j] + t[j] == 4:
            print 'O won'
            cont_flag = True
            break
    if cont_flag:
        continue
    print 'Game has not completed' if dot else 'Draw'