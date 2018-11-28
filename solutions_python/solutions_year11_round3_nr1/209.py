#!/usr/bin/python
import sys
import fractions

#f = open( 'A-small-attempt0.in' )
#f = open( 'input.txt' )
#rl = lambda: f.readline().strip()
rl = lambda: sys.stdin.readline().strip()


class Pos:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Point:
    def __init__(self, char, pos, size):
        self.Char = char
        self.Pos = pos
        self.Size = size
        
    def calcCornerOrder(self, array):
        order = 0
        if self.Pos.x <= 0 or array[ self.Pos.y ][ self.Pos.x - 1 ].Char != '#':
            order += 1
        if self.Pos.x >= self.Size.x - 1 or array[ self.Pos.y ][ self.Pos.x + 1 ].Char != '#':
            order += 1
        if self.Pos.y <= 0 or array[ self.Pos.y - 1 ][ self.Pos.x ].Char != '#':
            order += 1
        if self.Pos.y >= self.Size.y - 1 or array[ self.Pos.y + 1 ][ self.Pos.x ].Char != '#':
            order += 1
        return order
        
    def canConvert(self, array, x, y ):
        if self.Pos.y + y < 0 or self.Pos.y + y >= self.Size.y:
            return False
        if self.Pos.x + x < 0 or self.Pos.x + x >= self.Size.x:
            return False
        if not array[ self.Pos.y + y ][ self.Pos.x ].Char == '#':
            return False
        if not array[ self.Pos.y ][ self.Pos.x + x ].Char == '#':
            return False
        if not array[ self.Pos.y + y ][ self.Pos.x + x ].Char == '#':
            return False
        return True
    
    def convert(self, array, x, y, mine, other ):
        array[ self.Pos.y ][ self.Pos.x ].Char = mine
        array[ self.Pos.y + y ][ self.Pos.x ].Char = other
        array[ self.Pos.y ][ self.Pos.x + x ].Char = other
        array[ self.Pos.y + y ][ self.Pos.x + x ].Char = mine
        


def check( rows ):
    while True:
        progress = False
        max = None
        maxOrder = 0
        
        for cols in rows:
            for p in cols:
                if p.Char == '#':
                    progress = True
                    order = p.calcCornerOrder( rows )
                    
                    # impossible
                    if order >= 3:
                        return ''
                    
                    if maxOrder < order:
                        max = p
                        maxOrder = order
                        
        
        if not progress:
            break
        
        
        if maxOrder == 0:
            assert False
            
        
        if max.canConvert( rows, -1, -1 ):
            max.convert( rows, -1, -1, '/', '\\' )
        elif max.canConvert( rows, -1, 1 ):
            max.convert( rows, -1, 1, '\\', '/' )
        elif max.canConvert( rows, 1, -1 ):
            max.convert( rows, 1, -1, '\\', '/' )
        elif max.canConvert( rows, 1, 1 ):
            max.convert( rows, 1, 1, '/', '\\' )
        else:
            return ''
            
            
    result = []
    for cols in rows:
        line = ''
        for col in cols:
            line += col.Char
        result.append( line )
        
    return result


cases = int( rl() )

for cc in range( cases ):
    
    r, c = map( int, rl().split() )
    #print( '{} {} {}'.format( n, pd, pg ))
    
    size = Pos( c, r )
    rows = []
    for row in range( r ):
        cols = []
        line = rl()
        for col in range( c ):
            tile = line[ col ]
            cols.append( Point( tile, Pos( col, row ), size ) )
        rows.append( cols )
    
    result = check( rows )
    print( "Case #{}:".format( cc + 1 ) )
    if result == '':
        print( "Impossible".format( cc + 1 ) )
    else:
        for row in result:
            print( row )
