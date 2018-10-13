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

def sig ( s ):
    return sum([ (1<<i) for i in s ])

def P( s, C ):
    #print [ (k,v) for k, v in C.iteritems() if cross(s, k) ]
    a = sum( ( v for k, v in C.iteritems() if cross(s, k) ) )
    #print s, a
    return a

def cross( a, b ):
    return (a & b) and ((~a) & b)

def solve( N, Z ):
    R = defaultdict(set)
    for r, line in enumerate(Z):
        for word in line:
            R[word].add(r)
    #print R
    C = defaultdict(int)
    for v in R.itervalues():
        C[sig(v)] += 1
    #print C
    x = (1 << N) + 2
    return min( ( P( x +(i<<2), C ) for i in range( 1<<(N-2) ) ) )
        

def main(f):
    T = int( f.next() )
    for i in range(T):
        N = int( f.next() )
        Z = [ f.next().strip().split() for k in range(N) ]
        print "Case #{0}: {1}".format( i+1, solve( N, Z ) )

if len(sys.argv) >= 2:
    main(open(sys.argv[1]))
else:
    main(   StringIO.StringIO(  """\
4
2
he loves to eat baguettes
il aime manger des baguettes
4
a b c d e
f g h i j
a b c i j
f g h d e
4
he drove into a cul de sac
elle a conduit sa voiture
il a conduit dans un cul de sac
il mange pendant que il conduit sa voiture
6
adieu joie de vivre je ne regrette rien
adieu joie de vivre je ne regrette rien
a b c d e
f g h i j
a b c i j
f g h d e
""" ))
