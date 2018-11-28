def gcd( x, y) :
    if ( 0 == x ):
        return y;
    if ( 0 == y ):
        return x
    return gcd( y, x%y )

caseNum=int(input())
for caseId in range(caseNum):
    N, Pd, Pg = raw_input().split()
    N=int(N)
    Pd=int(Pd)
    Pg=int(Pg)

    #print N, Pd, Pg

    result = "Broken"
    if ( 0 == Pg and Pd != 0 ):
        pass
    elif ( 0 ==Pg and Pd == 0 ):
        result = "Possible"
    elif ( Pg == 100 and Pd != 100 ):
        pass
    elif ( 100 == Pg and Pd == 100 ):
        result = "Possible"    
    elif ( N < 100 / gcd( Pd, 100 ) ):
        pass
    else:
        result = "Possible"

    print "Case #%d: %s" % (caseId+1, result)
