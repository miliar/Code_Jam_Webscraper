import sys
import numpy as np

def process_file( fin, fout ):
    def get_one_problem():
        N, M = map( int, fin.readline().split() )
        lawn = np.arange( N*M ).reshape((N, M))
        for i in range( N ):
            lawn[i,:] = map( int, fin.readline().split() )
        return (N, M, lawn)

    num_cases = int( fin.readline() )
    for i in range( num_cases ):
        N, M, lawn = get_one_problem()
        print lawn
        s = solve_one_problem( N, M, lawn )
        fout.write( "Case #%d: %s\n" % (i+1,s) )

def solve_one_problem( N, M, lawn ):
    mins = np.argmin( lawn, 0 )
    for c in range( len( mins ) ):
        r = mins[c]
        m = lawn[r][c]
        if all( lawn[:,c] == m ):
            continue
        rows = np.where( lawn[:,c] == m )
        for r in rows[0]:
            if not ( all( lawn[r,:] == m ) ):
                return "NO"

    return "YES"

process_file( open(sys.argv[1]), open(sys.argv[1].replace("in", "out"), "w") )
