import psyco
import sys
#import scipy.sparse

psyco.full()


def read_integer():
    return int( sys.stdin.readline() )

def read_integer_list():
    return [ int( x ) for x in sys.stdin.readline().split() ]

def read_string():
    return sys.stdin.readline().strip()

C = read_integer()

for c in range( C ):
    print 'Case #%i:' % ( c + 1 ),
    R = read_integer()
    #grid = scipy.sparse.dok_matrix( ( limit, limit ), dtype = scipy.byte )
    #new_grid = scipy.sparse.dok_matrix( ( limit, limit ), dtype = scipy.byte )
    #grid = scipy.zeros( ( limit, limit ), dtype = scipy.byte )
    #new_grid = scipy.zeros( ( limit, limit ), dtype = scipy.byte )
    grid = {}
    #grid = [ [ 0 ]*limit ]*limit
    #new_grid = [ [ 0 ]*limit ]*limit
    rectangles = []
    for r in range( R ):
        X1, Y1, X2, Y2 = read_integer_list()
        rectangles.append( [ X1, Y1, X2 + 1, Y2 + 1 ] )
        for x in range( X1, X2 + 1 ):
            for y in range( Y1, Y2 + 1 ):
                grid[ (x, y) ] = True
    seconds = 0
    while grid:
        new_grid = {}
        for cell in grid:
            x, y = cell
            if ( x - 1, y ) in grid or ( x, y - 1 ) in grid:
                new_grid[ cell ] = True
            if ( x, y + 1 ) not in grid and ( x - 1, y + 1 ) in grid:
                new_grid[ ( x, y + 1 ) ] = True
        seconds += 1
        grid = new_grid
    print seconds
