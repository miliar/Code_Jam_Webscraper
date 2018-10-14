from sys import stdin
import math

N = int(stdin.readline())
winner = ""

for case_idx in range(N):

    line = stdin.readline().strip().split(' ')
    X,R,C = float(line[0]),float(line[1]),float(line[2])

    # dimension of the grid
    grid = R*C

    if (grid % X) == 0:

        # size of the maximum dimension
        dim = math.ceil(X/2)
        
        if ( dim <= R ) and ( dim <= C ):
            if X == 4:
                if ( R == 2 ) or (C == 2):
                    winner = "RICHARD"
                else:
                    winner = "GABRIEL"        
            else:
                winner = "GABRIEL"
        else:
            winner = "RICHARD"
    else:
        winner = "RICHARD"

    print("Case #",str(case_idx+1),": ",str(winner),sep="")

