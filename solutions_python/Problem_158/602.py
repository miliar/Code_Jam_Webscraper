from sys import stdin

T = int(stdin.readline())
for i in range(1,T+1):
    X, R, C = [int(x) for x in stdin.readline().split()]
    winner = None
    if X == 1: winner = "GABRIEL"
    elif X == 2:
        if R % 2 == 1 and C % 2 == 1: winner = "RICHARD"
        else: winner = "GABRIEL"
    elif X == 3:
        if R == 1 or C == 1: winner = "RICHARD"
        elif (R % 2 == 0 and C % 3 != 0) or (C % 2 == 0 and R % 3 != 0):
            winner = "RICHARD"
        else: winner = "GABRIEL"
    else:
        if R <= 2 or C <= 2 or (R == 3 and C == 3): winner = "RICHARD"
        else: winner = "GABRIEL"
    print("Case #{0}: {1}".format(i,winner))

