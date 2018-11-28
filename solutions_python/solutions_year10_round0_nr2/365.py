import sys

def gcd(a, b):
    if b == 0: return a
    return gcd(b, a % b)
    
sys.stdin.readline()
count = 0
    
for line in sys.stdin:
    count += 1
    a = map( int, line.split( ' ' ) )[1:]
    a.sort()
##     print a

    diffs = []
    for i in xrange( len( a ) - 1 ):
        diffs.append( a[i+1] - a[i] )
    if( len( diffs ) > 1 ):
        cur = gcd( diffs[0], diffs[1] )
        for i in xrange( 2, len( diffs ) ):
            cur = gcd( cur, diffs[i] )
    else:
        cur = diffs[0]
    i = a[0] / cur
    while 1:
        if( cur * i - a[0] >= 0 ):
            cur = cur * i - a[0]
            break
        i += 1
        
    print 'Case #%d: %d' % (count, cur )
        
    
    
