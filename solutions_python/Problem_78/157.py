#!/usr/bin/python
import sys
import fractions

#f = open( 'input.txt' )
#rl = lambda: f.readline().strip()
rl = lambda: sys.stdin.readline().strip()

gcd = fractions.gcd

def check( n, pd, pg, ld, lg ):
    if pg == 100 or pg == 0:
        return True if pd == pg else False
    
    baseD = 100 // gcd( 100, pd )
    baseG = 100 // gcd( 100, pg )
    
    if baseD > n:
        return False
    
    return True


cases = int( rl() )

for cc in range( cases ):
    
    n, pd, pg = map( int, rl().split() )
    ld, lg = ( 100 - pd, 100 - pg )
    #print( '{} {} {}'.format( n, pd, pg ))
    
    result = check( n, pd, pg, ld, lg )
    if result:
        result = 'Possible'
    else:
        result = 'Broken'
    
    print( "Case #{}: {}".format( cc + 1, result ) )
