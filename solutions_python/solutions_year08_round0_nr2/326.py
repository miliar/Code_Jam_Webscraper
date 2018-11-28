#!/usr/bin/env python

import sys

import psyco
psyco.full()


class Case:
    def __init__( self, stream ):
        self.turntime = int( stream.readline() )

        ns = [ int(x) for x in stream.readline().split() ]
        times = []
        for n in ns:
            times.append( self.__readSection( stream, n ) )

        queues = [ [] for i in range( len( times ) ) ]
        for i in range( len( times ) ):
            for dep, arr in times[i]:
                queues[i].append( ( dep, -1 ) )
                queues[i-1].append( ( arr+self.turntime, +1 ) )

        for q in queues:
            q.sort( self.__cmp )
        self.queues = queues

    def __readSection( self, stream, N ):
        result = []
        for i in range( N ):
            dep, arr = [ self.__convTime( x ) for x in stream.readline().split() ]
            result.append( ( dep, arr ) )
        return result

    def __convTime( self, timeStr ):
        h, m = [ int(x) for x in timeStr.split(':') ]
        return h*60+m

    def __cmp( self, a, b ):
        if a[0] == b[0]:
            return (b[1]-a[1])/2
        elif a[0] < b[0]:
            return -1
        else:
            return 1

    def solve( self ):
        result = []
        for queue in self.queues:
            pool = 0
            trains = 0
            for time, op in queue:
                pool += op
                if pool < 0:
                    trains += 1
                    pool = 0

            result.append( trains )

        return result


def log( msg ):
    print >>sys.stderr, msg

def main( args ):
    stream = sys.stdin
    N = int( stream.readline() )
    log( "Number of test cases: %d" % N )
    for i in range( N ):
        c = Case( stream )
        print "Case #%d: %s" % ( i+1, ' '.join( [ str(x) for x in c.solve() ] ) )

main( sys.argv )

