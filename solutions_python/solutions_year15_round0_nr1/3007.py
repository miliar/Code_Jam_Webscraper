test_cases = raw_input()

for i in xrange( 0, int( test_cases ) ):
    # extract row info
    row = raw_input().split()
    ( max_shy, audience ) = ( row[ 0 ], row[ 1 ] )

    # analyse
    friends_needed = 0
    current_clapping = 0
    for shyness, element in enumerate( audience ):
        # add friends to ensure everyone at this level claps
        if int( element ) > 0 and shyness > current_clapping:
            bring_friends = ( shyness - current_clapping )
            friends_needed += bring_friends
            current_clapping += bring_friends
        current_clapping += int( element )
    print 'Case #{0}: {1}'.format( i + 1, friends_needed )
