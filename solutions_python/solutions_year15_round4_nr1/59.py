import sys, itertools as itt, StringIO
#import heapq, bisect, numpy, math
from collections import defaultdict, namedtuple, deque, Counter
from operator import itemgetter
from types import FunctionType

lines = lambda f: "\n".join( map( str, f ) )
def linearg ( f, fmt = None ):
    if fmt == None:
        return f.next().strip().split()
    elif isinstance( fmt, (type,FunctionType) ):
        return [ fmt(i) for i in f.next().strip().split() ]
    else:
        return [ i(j) for i, j in zip( fmt, f.next().strip().split() ) ]

class Graph ( defaultdict ):
    def __init__ ( self, pairs ):
        defaultdict.__init__( self, list )
        for i, j in pairs:
            self[i].append(j)
            self[j].append(i)

def solve( R, C, Z ):
    M = defaultdict( list )
    for r in range(R):
        for c in range(C):
            if Z[r][c] != '.':
                M[ (r,c) ].append( '<' )
                break
        for c in range(C-1, -1, -1):
            if Z[r][c] != '.':
                M[ (r,c) ].append( '>' )
                break
    for c in range(C):
        for r in range(R):
            if Z[r][c] != '.':
                M[ (r,c) ].append( '^' )
                break
        for r in range(R-1, -1, -1):
            if Z[r][c] != '.':
                M[ (r,c) ].append( 'v' )
                break
    n = 0
    for (r,c), avoid in M.iteritems():
        if len(avoid)==4:
            return "IMPOSSIBLE"
        if Z[r][c] in avoid:
            n += 1
    return n

def main(f):
    T = int( f.next() )
    for i in range(T):
        R, C = linearg( f, int )
        Z = [ f.next().strip() for k in range(R) ]
        print "Case #{0}: {1}".format( i+1, solve( R, C, Z ) )

if len(sys.argv) >= 2:
    main(open(sys.argv[1]))
else:
    main(   StringIO.StringIO(  """\
4
2 1
^
^
2 2
>v
^<
3 3
...
.^.
...
1 1
.""" ))

