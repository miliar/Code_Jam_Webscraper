f = open( "A-large.in" )

numcases = int(f.readline( ).strip( ) )


for x in xrange(numcases):
    (P, K, L) = map(int, f.readline( ).strip( ).split( " ") )
    message = zip( map(int, f.readline( ).strip( ).split( " ") ), xrange(L ) )
    message.sort( )
    message.reverse( )
#    print message
    total = 0
    key = 0
    letternum = 1
    for (fr,m) in message:
        total += (letternum * fr)
        key += 1
        if key == K:
            key = 0
            letternum += 1
    print "Case #%s: %s" % (x+1,total)

    
