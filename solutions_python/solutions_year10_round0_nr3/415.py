
f = open( "C-small-attempt0.in" )
caseCount = int( f.readline() )


for x in xrange( caseCount ):
    R , k , N = map( int , f.readline().split(' ') )
    nList = map( int , f.readline().split(' ') )

    money = 0 
    listSize = len( nList )
    for y in xrange( R ):

        # assign person
        for z in xrange( 1 , listSize + 1 ):
            personCount = sum( nList[:z] )
            if personCount > k :
                break
        else:
            money += sum( nList )
            continue

        money += sum( nList[:z-1] )
        nList = nList[z-1:] + nList[:z-1]

    print "Case #%d: %d" % ( x + 1 , money )



        

