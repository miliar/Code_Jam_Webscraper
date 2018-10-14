import os
import sys 
import string

v = sys.stdin.readline();
i = 1
for line in sys.stdin: 
    w = string.split( line ) 
    n = int( w[0] );
    k = int( w[1] );
    sys.stdout.write( 'Case #' ); 
    sys.stdout.write( str( i ) ); 
    sys.stdout.write( ': ' ); 
    if(  ( k % pow( 2, n ) ) == (pow( 2, n) -1 ) ):   
        print "ON"
    else:
        print "OFF"
    i = i + 1

