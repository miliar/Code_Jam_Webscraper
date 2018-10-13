d = {
(1, 1, 1):"GABRIEL",
(2, 1, 1):"RICHARD",
(3, 1, 1):"RICHARD",
(4, 1, 1):"RICHARD",
(1, 1, 2):"GABRIEL",
(2, 1, 2):"GABRIEL",
(3, 1, 2):"RICHARD",
(4, 1, 2):"RICHARD",
(1, 1, 3):"GABRIEL",
(2, 1, 3):"RICHARD",
(3, 1, 3):"RICHARD",
(4, 1, 3):"RICHARD",
(1, 1, 4):"GABRIEL",
(2, 1, 4):"GABRIEL",
(3, 1, 4):"RICHARD",
(4, 1, 4):"RICHARD",
(1, 2, 1):"GABRIEL",
(2, 2, 1):"GABRIEL",
(3, 2, 1):"RICHARD",
(4, 2, 1):"RICHARD",
(1, 2, 2):"GABRIEL",
(2, 2, 2):"GABRIEL",
(3, 2, 2):"RICHARD",
(4, 2, 2):"RICHARD",
(1, 2, 3):"GABRIEL",
(2, 2, 3):"GABRIEL",
(3, 2, 3):"GABRIEL",
(4, 2, 3):"RICHARD",
(1, 2, 4):"GABRIEL",
(2, 2, 4):"GABRIEL",
(3, 2, 4):"RICHARD",
(4, 2, 4):"RICHARD",
(1, 3, 1):"GABRIEL",
(2, 3, 1):"RICHARD",
(3, 3, 1):"RICHARD",
(4, 3, 1):"RICHARD",
(1, 3, 2):"GABRIEL",
(2, 3, 2):"GABRIEL",
(3, 3, 2):"GABRIEL",
(4, 3, 2):"RICHARD",
(1, 3, 3):"GABRIEL",
(2, 3, 3):"RICHARD",
(3, 3, 3):"GABRIEL",
(4, 3, 3):"RICHARD",
(1, 3, 4):"GABRIEL",
(2, 3, 4):"GABRIEL",
(3, 3, 4):"GABRIEL",
(4, 3, 4):"GABRIEL",
(1, 4, 1):"GABRIEL",
(2, 4, 1):"GABRIEL",
(3, 4, 1):"RICHARD",
(4, 4, 1):"RICHARD",
(1, 4, 2):"GABRIEL",
(2, 4, 2):"GABRIEL",
(3, 4, 2):"RICHARD",
(4, 4, 2):"RICHARD",
(1, 4, 3):"GABRIEL",
(2, 4, 3):"GABRIEL",
(3, 4, 3):"GABRIEL",
(4, 4, 3):"GABRIEL",
(1, 4, 4):"GABRIEL",
(2, 4, 4):"GABRIEL",
(3, 4, 4):"RICHARD",
(4, 4, 4):"GABRIEL",
}
def generate_pieces(X):
    # this isn't defined very nicely
    for x in range(1, X + 1): # all the 'corner' pieces
        # yields (rowsUsed, columnsUsed)
        yield (x, X + 1 - x)

def can_place(piece, R, C):
    #return piece[0] <= C and piece[1] <= R
    return (piece[0] <= C and piece[1] <= R) or (piece[0] <= R and piece[1] <= C)

T = int(input())
#print("{")
for t in range(1, T+1):
    X, R, C = [int(x) for x in input().split()]
    """
    winner = None
    if ((R * C) - X) % X == 0:
        pieces = generate_pieces(X)
        winner = 'GABRIEL'
        for piece in pieces:
            if not can_place(piece, R, C):
                winner = 'RICHARD'
                break
    else:
        winner = 'RICHARD'
    print((X, R, C),":",winner)
    """
    print("Case #{0}: {1}".format(t, d[(X,R,C)]))
#print("}")
