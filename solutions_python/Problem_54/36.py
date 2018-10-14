
import math

def gcd(a, b) :
    if b == 0 :
        return a
    return gcd( b , a % b )

def abs( x ) :
    if x < 0 : return -x
    return x

TNO = int( raw_input() )
for tno in range(TNO) :
    line = raw_input().split(' ')
    a = [int(token) for token in line[1:]]
    N = len(a)
    
    g = -1
    for i in range(N) :
        for j in range(i) :
            if g == -1 :
                g = abs( a[i] - a[j] )
            else :
                g = gcd( g, abs( a[i] - a[j] ) )
    
    print "Case #" + str(tno + 1) + ":", (g - a[0] % g) % g
    
