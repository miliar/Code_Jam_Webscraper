#!/usr/bin/python

import sys

# r 1 y 2 b 4
# o 3 g 6 v 5

def solve( N,R,O,Y,G,B,V ):

    #print( "doing ", N,R,O,Y,G,B,V )

    # single r,y,b
    # ry = o
    # rb = b
    # by = g

    reds = R + O + V
    blues = B + V + G
    yells = Y + O + G

    half = N/2
    if ( reds > half or blues > half or yells > half ):
        return "IMPOSSIBLE"

    l = []
    r = []
    prev = 0
    for i in range( N ):

        reds = R + O + V
        blues = B + V + G
        yells = Y + O + G
        most = max(reds,blues,yells)
        #print( reds, blues, yells, most, i  )

        
    
        if ( most == reds ):
            if ( yells >= blues ): 
                if ( O >= 1 and ( 3 & prev ) == 0 ):
                    O = O - 1
                    if ( i == 0 ):
                        O = O + 0.5
                    l.append("O")
                    r.append(3)
                    prev = 3
                elif ( V >= 1 and ( 5 & prev ) == 0 ):
                    V = V - 1
                    if ( i == 0 ):
                        V = V + 0.5
                    l.append("V")
                    r.append(5)
                    prev = 5
                elif ( R >= 1 and ( 1 & prev ) == 0 ):
                    R = R - 1
                    if ( i == 0 ):
                        R = R + 0.5
                    l.append("R")
                    r.append(1)
                    prev = 1
                elif ( G >= 1 and ( 6 & prev ) == 0 ):
                    G = G - 1
                    if ( i == 0 ):
                        G = G + 0.5
                    l.append("G")
                    r.append(6)
                    prev = 6
                elif ( Y >= 1 and ( 2 & prev ) == 0 ):
                    Y = Y - 1
                    if ( i == 0 ):
                        Y = Y + 0.5
                    l.append("Y")
                    r.append(2)
                    prev = 2
                elif ( B >= 1 and ( 4 & prev ) == 0 ):
                    B = B - 1
                    if ( i == 0 ):
                        B = B + 0.5
                    l.append("B")
                    r.append(4)
                    prev = 4
                else:
                    raise Exception( "Should not happen! " + str(i) )
            else: 
                if ( V >= 1 and ( 5 & prev ) == 0 ):
                    V = V - 1
                    if ( i == 0 ):
                        V = V + 0.5
                    l.append("V")
                    r.append(5)
                    prev = 5
                elif ( O >= 1 and ( 3 & prev ) == 0 ):
                    O = O - 1
                    if ( i == 0 ):
                        O = O + 0.5
                    l.append("O")
                    r.append(3)
                    prev = 3
                elif ( R >= 1 and ( 1 & prev ) == 0 ):
                    R = R - 1
                    if ( i == 0 ):
                        R = R + 0.5
                    l.append("R")
                    r.append(1)
                    prev = 1
                elif ( G >= 1 and ( 6 & prev ) == 0 ):
                    G = G - 1
                    if ( i == 0 ):
                        G = G + 0.5
                    l.append("G")
                    r.append(6)
                    prev = 6
                elif ( B >= 1 and ( 4 & prev ) == 0 ):
                    B = B - 1
                    if ( i == 0 ):
                        B = B + 0.5
                    l.append("B")
                    r.append(4)
                    prev = 4
                elif ( Y >= 1 and ( 2 & prev ) == 0 ):
                    Y = Y - 1
                    if ( i == 0 ):
                        Y = Y + 0.5
                    l.append("Y")
                    r.append(2)
                    prev = 2
                else:
                    raise Exception( "Should not happen! " + str(i) )
        elif ( most == blues ):
            if ( reds >= yells ):
                if ( V >= 1 and ( 5 & prev ) == 0 ):
                    V = V - 1
                    if ( i == 0 ):
                        V = V + 0.5
                    l.append("V")
                    r.append(5)
                    prev = 5
                elif ( G >= 1 and ( 6 & prev ) == 0 ):
                    G = G - 1
                    if ( i == 0 ):
                        G = G + 0.5
                    l.append("G")
                    r.append(6)
                    prev = 6
                elif ( B >= 1 and ( 4 & prev ) == 0 ):
                    B = B - 1
                    if ( i == 0 ):
                        B = B + 0.5
                    l.append("B")
                    r.append(4)
                    prev = 4
                elif ( O >= 1 and ( 3 & prev ) == 0 ):
                    O = O - 1
                    if ( i == 0 ):
                        O = O + 0.5
                    l.append("O")
                    r.append(3)
                    prev = 3
                elif ( R >= 1 and ( 1 & prev ) == 0 ):
                    R = R - 1
                    if ( i == 0 ):
                        R = R + 0.5
                    l.append("R")
                    r.append(1)
                    prev = 1
                elif ( Y >= 1 and ( 2 & prev ) == 0 ):
                    Y = Y - 1
                    if ( i == 0 ):
                        Y = Y + 0.5
                    l.append("Y")
                    r.append(2)
                    prev = 2
                else:
                    raise Exception( "Should not happen! " + str(i) )
            else:
                if ( G >= 1 and ( 6 & prev ) == 0 ):
                    G = G - 1
                    if ( i == 0 ):
                        G = G + 0.5
                    l.append("G")
                    r.append(6)
                    prev = 6
                elif ( V >= 1 and ( 5 & prev ) == 0 ):
                    V = V - 1
                    if ( i == 0 ):
                        V = V + 0.5
                    l.append("V")
                    r.append(5)
                    prev = 5
                elif ( B >= 1 and ( 4 & prev ) == 0 ):
                    B = B - 1
                    if ( i == 0 ):
                        B = B + 0.5
                    l.append("B")
                    r.append(4)
                    prev = 4
                elif ( O >= 1 and ( 3 & prev ) == 0 ):
                    O = O - 1
                    if ( i == 0 ):
                        O = O + 0.5
                    l.append("O")
                    r.append(3)
                    prev = 3
                elif ( Y >= 1 and ( 2 & prev ) == 0 ):
                    Y = Y - 1
                    if ( i == 0 ):
                        Y = Y + 0.5
                    l.append("Y")
                    r.append(2)
                    prev = 2
                elif ( R >= 1 and ( 1 & prev ) == 0 ):
                    R = R - 1
                    if ( i == 0 ):
                        R = R + 0.5
                    l.append("R")
                    r.append(1)
                    prev = 1
                else:
                    raise Exception( "Should not happen! " + str(i) )
        elif ( most == yells ):
            if ( reds >= blues ):
                if ( O >= 1 and ( 3 & prev ) == 0 ):
                    O = O - 1
                    if ( i == 0 ):
                        O = O + 0.5
                    l.append("O")
                    r.append(3)
                    prev = 3
                elif ( G >= 1 and ( 6 & prev ) == 0 ):
                    G = G - 1
                    if ( i == 0 ):
                        G = G + 0.5
                    l.append("G")
                    r.append(6)
                    prev = 6
                elif ( Y >= 1 and ( 2 & prev ) == 0 ):
                    Y = Y - 1
                    if ( i == 0 ):
                        Y = Y + 0.5
                    l.append("Y")
                    r.append(2)
                    prev = 2
                elif ( V >= 1 and ( 5 & prev ) == 0 ):
                    V = V - 1
                    if ( i == 0 ):
                        V = V + 0.5
                    l.append("V")
                    r.append(5)
                    prev = 5
                elif ( R >= 1 and ( 1 & prev ) == 0 ):
                    R = R - 1
                    if ( i == 0 ):
                        R = R + 0.5
                    l.append("R")
                    r.append(1)
                    prev = 1
                elif ( B >= 1 and ( 4 & prev ) == 0 ):
                    B = B - 1
                    if ( i == 0 ):
                        B = B + 0.5
                    l.append("B")
                    r.append(4)
                    prev = 4
                else:
                    raise Exception( "Should not happen! " + str(i) )
            else:
                if ( G >= 1 and ( 6 & prev ) == 0 ):
                    G = G - 1
                    if ( i == 0 ):
                        G = G + 0.5
                    l.append("G")
                    r.append(6)
                    prev = 6
                elif ( O >= 1 and ( 3 & prev ) == 0 ):
                    O = O - 1
                    if ( i == 0 ):
                        O = O + 0.5
                    l.append("O")
                    r.append(3)
                    prev = 3
                elif ( Y >= 1 and ( 2 & prev ) == 0 ):
                    Y = Y - 1
                    if ( i == 0 ):
                        Y = Y + 0.5
                    l.append("Y")
                    r.append(2)
                    prev = 2
                elif ( V >= 1 and ( 5 & prev ) == 0 ):
                    V = V - 1
                    if ( i == 0 ):
                        V = V + 0.5
                    l.append("V")
                    r.append(5)
                    prev = 5
                elif ( B >= 1 and ( 4 & prev ) == 0 ):
                    B = B - 1
                    if ( i == 0 ):
                        B = B + 0.5
                    l.append("B")
                    r.append(4)
                    prev = 4
                elif ( R >= 1 and ( 1 & prev ) == 0 ):
                    R = R - 1
                    if ( i == 0 ):
                        R = R + 0.5
                    l.append("R")
                    r.append(1)
                    prev = 1
                else:
                    raise Exception( "Should not happen! " + str(i) )

    
    if ( (r[0] & r[-1]) != 0 ):
        return "IMPOSSIBLE"
        s =  "".join(l)  
        raise Exception("Should never happen! " + s  )


    return "".join(l)
    

testcases = int( sys.stdin.readline() )
for i in range( testcases ):

    data = [ int(x) for x in sys.stdin.readline().strip().split() ]
    print( "Case #{}: {}".format( i+1, solve(data[0],data[1],data[2],data[3],data[4],data[5],data[6] ) ) )



