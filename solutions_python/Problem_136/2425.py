T = int( input() )
for Ti in range( 1, T+1 ):
    C, F, X = [ float(v) for v in input().split() ]

    Fn = 0
    Fs = 0
    Fp = 2
    prevs = X/Fp
    curs = prevs

    while curs <= prevs:
        prevs = curs
        Fs += C/Fp
        Fn += 1
        Fp += F
        curs = Fs + X/Fp

        #print( "Fn Fp Fs curs", Fn, Fp, Fs, curs )

    print( "Case #{0}: {1}".format( Ti, prevs ) )