import sys

class Node:
    name = None
    children = []

    def __init__( self ):
        self.children = []
        self.name = ""

dirs = {}

def add_dir( path ):
    n = 0
    global dirs
    p = path.split('/')
    act = dirs
    for i in p:
        if len( i ) == 0:
            continue
        if act.get( i ) is None:
            n += 1
        act[ i ] = act.get( i, {} )
        act = act[ i ]
    return n




T = int( sys.stdin.readline().strip() )
for t in range(T):
    dirs = {}

    N, M = map( int, sys.stdin.readline().strip().split(' ' ) )
    for i in range(N):
        ln = sys.stdin.readline().strip()
        add_dir( ln )
    
    x = 0
    for i in range(M):
        ln = sys.stdin.readline().strip()
        x += add_dir( ln )
    
    print 'Case #%d: %d' % ( t+1, x, )

