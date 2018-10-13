import math
from array import array

t = int(input())

def output( x ):
    global a , b
    l = str(input()).split(' ')
    a = int(l[ 0 ])
    b = int(l[ 1 ])
    print ( "Case" , "#{0}:".format( x ) , fq[ b ] - fq[ a - 1 ] )

def is_p( x ):
    a = []
    l , r = 0 , 0
    while x != 0:
        a.append( x % 10 )
        x = int( x / 10 )
        r += 1
    #print( x , r , a )
    while l <= r - 1:
        if a[ l ] != a[ r - 1 ]:
            return False
        l += 1
        r -= 1
    return True

def sol_small():
    global fq
    d = dict()
    fq = [ 0 for i in range( 0 , 1001 ) ]

    for i in range( 1 , 1001 ):
        if( is_p( i ) ):
            d.update( [ ( i , True ) ] )
        
    for t in d:
        if d.get( math.sqrt( t ) ) != None:
            fq[ t ] = 1

    #print( fq )

    for i in range( 1 , 1001 ):
        fq[ i ] = fq[ i ] + fq[ i - 1 ]

    #print( fq )

sol_small()
for i in range( 0 , t ):
    output( i + 1 )

