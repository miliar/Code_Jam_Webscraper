import sys

def read_integer():
    return int( sys.stdin.readline() )

def read_integer_line():
    return [ int( x ) for x in sys.stdin.readline().split() ]

def read_string():
    return sys.stdin.readline().strip()

T = read_integer()


def add( path ):
    cost = 0
    level = root
    for folder in path:
        if folder not in level:
            level[ folder ] = {}
            cost += 1
        level = level[ folder ]
    return cost


for t in range( T ):
    N, M = read_integer_line()
    total = 0
    root = {}
    for n in range( N ):
        add( read_string()[ 1 : ].split( '/' ) )
    for m in range( M ):
        total += add( read_string()[ 1 : ].split( '/' ) )
    print 'Case #%i:' % ( t + 1 ), total
