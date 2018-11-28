def maxDevide( x , y ):
    if x > y :
        m = x
        n = y
    else:
        m = y 
        n = x 

    while True:
        tmp = m % n 
        if tmp == 0 :
            break

        t = n ;
        n = tmp
        m = t

    return n



def maxDevideM( argsList , offset = 0 ):
    ret = argsList[0] + offset 
    for index in xrange( 1 , len( argsList ) ):
        ret = maxDevide( ret , argsList[index] + offset )
    return ret



def checkValid( argsList , D , R ):
    for x in argsList:
        if ( x + R ) % D == 0 :
            continue
        else:
            return False

    return True




f = open( "B-small-attempt4.in" )
caseCount = int( f.readline() )


for x in xrange( caseCount ):
    argsList = map( int , f.readline().split(' ') )[1:]
    minusList = []
    for _x in xrange( len( argsList ) ):
        for _y in xrange( _x + 1 , len( argsList ) ):
            minusList.append( argsList[_x] - argsList[_y] )

    minusList = map( abs , minusList )
    try:
        minusList.remove( 0 )
    except:
        pass
    try:
        minusList.index( 1 )
        print "Case #%d: %d" % ( x + 1 , 0 )
        continue
    except:
        pass

    dev = maxDevideM( minusList )
    finalBase = 0 
    total = sum( argsList )
    while finalBase < total :
        finalBase += dev

    length = len( argsList )
    while True:
        tmp = finalBase - total 
        if tmp % length == 0 and checkValid( argsList , dev , tmp / length ):
            break
        else:
            finalBase += dev

    print "Case #%d: %d" % ( x + 1 , tmp / length )


