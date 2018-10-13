# To run this on an input file called sample.in, use the following
# command line:
#
# python fireflies2.py sample.in
#
# The output will appear on the console.  I used Python 2.5.2.
#
# NOTE: This applies to my short entry as well, except use fireflies.py!  I made a typo in the command
# line instructions.
import sys
from math import *
from decimal import *

if len( sys.argv ) < 2:
    print "Please provide input file."
    exit(1)

fp = open( sys.argv[1], 'rb' )
cases = int( fp.readline() )

def dsum(a):
    r = Decimal()
    for x in a:
        r += x
    print "Returning sum %s" % r
    return r

def dotProd(a,b):
    return sum( ( a[i] * b[i] for i in xrange(len(a)) ) )

def length(c):
    return sqrt(sum( ( x*x for x in c ) ))
    
for case in xrange( cases ):
    N = int( fp.readline() )
    terms = [0,0,0,0,0,0]
    for _ in xrange(N):
        tm = map(float, fp.readline().split());
        for i in xrange(6):
            terms[i] = terms[i] + tm[i]
    for i in xrange(6):
        terms[i] /= N
    
    # Project vector
    A = terms[0:3]
    B = terms[3:6]
    
    #print "Terms: %s, A: %s, B: %s" % ( terms, A, B )
    lenB = length( B )
    lenA = length( A )
    if ( lenB > 0 ):
        dp = dotProd( A, B )
        lenC = abs( dp / lenB )
    
        #print "A: %f, B: %f, C: %f" % ( lenA, lenB, lenC )
    
        diff = lenA**2 - lenC**2
        if diff <= 0:
            d = 0
        else:
            d = sqrt( lenA**2 - lenC**2 )
    
        t = lenC / lenB * ( 1 if dp < 0 else -1 )
        if t < 0:
            t = 0
            d = lenA
    else:
        t = 0
        d = lenA
    
    print "Case #%d: %f %f" % ( case + 1, d, t )