import sys

def gcd( a, b ):
    if b == 0: return a
    return gcd( b, a % b )

def get_gcd( l ):
    
    g = gcd( l[ 0 ], l[ 1 ] )
    for v in l[2:]:
        g = gcd( g, v )
    return g
    
def doit( l ):
    l.sort()
    diffs = []
    for i in xrange( 1, len(l )):
        diffs.append( l[ i ] - l[ i - 1] )
    if len(diffs) == 1:
        g = diffs[0]
    else:
        g = get_gcd( diffs )
        
    if l[0] % g  == 0:
        return 0
    return ((l[0] / g) * g + g) - l[0]



def main():
    for i, line in enumerate(sys.stdin):
        if i == 0: continue
        
        val = doit( map(long, line.strip().split(' '))[1:] )
        print "Case #%d: %d" % (i, val )
        

if __name__ == '__main__':
    main()
