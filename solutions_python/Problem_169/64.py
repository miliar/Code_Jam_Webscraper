import sys, itertools as itt, StringIO
#import heapq, bisect, numpy, math
import numpy as np
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

def solve( N, V, X, RC ):
    if N == 1:
        R, C = RC[0]
        if C == X:
            return V/R
        else:
            return "IMPOSSIBLE"
    if N == 2:
        R1, C1 = RC[0]
        R2, C2 = RC[1]
        if (C1 > X and C2 > X) or (C1 < X and C2 < X):
            return "IMPOSSIBLE"
        if C1 == X and C2 == X:
            return V/(R1+R2)  #max(R1,R2)
        if C1 == X:
            return V/R1
        if C2 == X:
            return V/R2
        A = np.array( [[ R1, R2 ], [ R1*C1, R2*C2 ]] )
        x = np.linalg.solve( A, [[V],[V*X]] )
        #V1 = V*(C2-X)/(C2-C1)
        #V2 = V*(C1-X)/(C1-C2)
        #return max( V1/R1, V2/R2 )
        return max(x)[0]


def main(f):
    T = int( f.next() )
    for i in range(T):
        N, V, X = linearg( f, float )
        N =  int(N)
        RC = [ linearg( f, float ) for k in range(N) ]
        ans = solve( N, V, X, RC )
        if isinstance( ans, str ):
            print "Case #{0}: {1}".format( i+1, ans )
        else:
            print "Case #{0}: {1:.12f}".format( i+1, ans )

if len(sys.argv) >= 2:
    main(open(sys.argv[1]))
else:
    main(   StringIO.StringIO(  """\
5
1 10.0000 50.0000
0.2000 50.0000
2 30.0000 65.4321
0.0001 50.0000
100.0000 99.9000
2 5.0000 99.9000
30.0000 99.8999
20.0000 99.7000
2 0.0001 77.2831
0.0001 97.3911
0.0001 57.1751
2 100.0000 75.6127
70.0263 75.6127
27.0364 27.7990
4 5000.0000 75.0000
10.0000 30.0000
20.0000 50.0000
300.0000 95.0000
40.0000 2.0000""" ))
