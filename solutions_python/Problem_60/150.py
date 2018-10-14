import sys

T = int( sys.stdin.readline().strip() )
for tt in range(T):
    N, K, B, TT = map( int, sys.stdin.readline().strip().split(' ' ) )
    xs = [ int(x) for x in sys.stdin.readline().strip().split(' ' )  ]
    vs = [ int(x) for x in sys.stdin.readline().strip().split(' ' )  ]

    dobeh = []
    finish = []
    for i in range( len( xs )-1 ):
        if vs[i] == vs[i+1]:
            t = -1
        else:
            t = ( xs[i+1] - xs[i] ) / float(vs[i] - vs[i+1])

        if t < 0:
            t = -1

        dobeh.append( t ) 

    for i in range( len( xs ) ):
        finish.append( (B - xs[i] )/float(vs[i]) )
    
    howmany = 0
    good = []
    for i, t in enumerate( finish ):
        if finish[len(finish)-i-1] <= TT:
            good.append( len(finish)-i-1 )
            howmany += 1
        else:
            break
    

    swaps = 0
    for i in range( K - howmany ):
        #print 'trying to swap'
        act = -1
        for x, f in enumerate( finish ):
            if f <= TT and not ( x in good ):
                act = x
        if act == -1:
            swaps = -1
            break

        #print act
        swaps += (N-1) - act - len(good)
        good.append( act )

    if swaps != -1:
        print 'Case #%d: %d' % ( tt+1, swaps, )
    else:
        print 'Case #%d: IMPOSSIBLE' % ( tt+1, )
    #print TT, K, howmany
    #print dobeh
    #print finish
