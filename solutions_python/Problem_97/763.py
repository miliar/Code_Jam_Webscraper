import sys
import math

precalc = []

def rotate( num, minV, maxV ):

    rots = set()
    rots.add( num )
    p = int( math.log( num, 10 ) )
    m = int(math.pow( 10, p + 1 ))
    x = num
    
    for a in range( 0, p ):
        x = x * 10 
        top = x / m 
        x = x + top
        x -= top * m 
        if x >= minV and x <= maxV:
            if x < num:
                return 0
            rots.add( int( x ) ) 

    lr = len( rots ) - 1
    res = 0;
    while lr > 0:
        res += lr
        lr -= 1 

    return res

def generateRots( min, max ):
    pairs = 0 
    for x in range( min, max + 1): 
        pairs += rotate( x, min, max )

    return pairs

generateRots( 1111, 2222 )

cnt = 0
for l in sys.stdin.readlines():
    if cnt > 0:
        numbers = map( lambda x: int( x ) , l.split() )
        print "Case #" + str( cnt ) + ": " + str( generateRots(numbers[0], numbers[1]) ) 
    cnt = cnt + 1 
