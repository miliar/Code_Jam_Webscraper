import sys

n = (int) (sys.stdin.readline().strip())
for i in range (1, n+1):
    X, R, C = [int(x) for x in sys.stdin.readline().strip().split(" ")]
    winner = "unknown case"
    if X > R and X > C: #Piece that won't fit
        winner = "RICHARD"
    elif (C * R) % X != 0: #Will overflow
        winner = "RICHARD"
    elif X == 1 and R >=1 and C >=1: #1-omino will always fit
        winner = "GABRIEL"
    elif X == 2 and (R % 2 == 0 or C % 2 == 0):
        #2-omino will wit as long as either row or col is even
        winner = "GABRIEL"
    elif X == 3: 
        if (R == 1 or C == 1): # will fail L 3-omino
            winner = "RICHARD"
        elif (R == 3 or C == 3):
            winner = "GABRIEL"
    elif X == 4:
        if C <= 2 or R <= 2: #will fail T, Z 4-omino
            winner = "RICHARD"
        elif C >= 3 or R >= 3:
            winner = "GABRIEL"
    print ("Case #{i}: {winner}".format(i=i, winner=winner))
    
