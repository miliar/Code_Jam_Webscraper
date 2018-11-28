T = int( input() )
for Ti in range( 1, T+1 ):
    Smax, S = [ i for i in input().split() ]
    Smax = int( Smax )
    S = [ int(i) for i in S ]

    friends = 0
    clapping = 0
    for i in range( Smax+1 ):
        if clapping < i:
            friends += i-clapping
            clapping = i
        clapping += S[i]

    print( "Case #{0}: {1}".format( Ti, friends ) )
