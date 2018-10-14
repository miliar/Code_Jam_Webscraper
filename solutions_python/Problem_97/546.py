def getmir( A ):
    result = []
    for i in range( 1, len( A ) ):
        v = A[i:] + A[:i]
        if v != A and v[0] != '0':
            result.append( A[i:] + A[:i] )
    return result

def check( A, B ):
    la, lb = len(A), len(B)
    va, vb = int(A), int(B)
    usage = set()
    for j in range( va, vb + 1 ):
        mir = getmir( str(j) )
        for bm in mir:
            ibm = int(bm)
            n, m =  min(j,ibm), max(j,ibm)
            if n >= va and n < m and m <= vb:
                if (n, m) not in usage:
                    usage.add( (n,m) )

    #print sorted( usage )
    return len( usage )

def problem():
    data = file( 'in', 'r' ).readlines()
    test_count = int( data[0] )
    for index, pair in enumerate( data[1: test_count +1] ):
        A, B = [ x for x in pair.split() ]
        print 'Case #%s: %s' % ( index + 1, check(A,B) )

if __name__ == "__main__":
    problem()
