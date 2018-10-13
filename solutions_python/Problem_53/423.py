def cycleCount( lightCount ):
    ret = 0
    for x in xrange( lightCount ):
        if x + 1 == 1 :
            ret = 1
        else:
            ret = ret * 2 + 1

    return ret

f = open( "A-large.in")
caseCount = int( f.readline() )

for x in xrange( caseCount ):
    lightCount , pressTime = map( int , f.readline().split(' ') )
    cycleBase = cycleCount( lightCount )

    if ( pressTime + 1 ) % ( cycleCount( lightCount ) + 1 ) == 0 :
        lightStatus = "ON"
    else:
        lightStatus = "OFF"
    print "Case #%d: %s" % ( x + 1 , lightStatus )
