def solveD():
    T = input()
    c = 0
    while c < T:
        c += 1
        [X, R, C] = map(int,raw_input().split())
        richard = doesRichardWin(X,R,C)
        result = "Case #%i: %s" % (c, "RICHARD" if richard else "GABRIEL")
        print result    
def doesRichardWin(X, R, C):
    if X == 1:
        return False #Gabriel wins for 1x1 pieces
    if R*C == 1:
        return True #Richard wins for 1x1 field with >1x1 pieces
    if X == 2:
        return (R * C) % 2 == 1 #Richard wins for uneven number of fields
    if X == 3:
        if (R*C)%3 != 0:
            return True #Richard wins for non-multiple of 3
        if R == 1 or C == 1:
            return True #Richard wins for 1xn or nx1
        return False # else it is possible
    # X = 4
    if (R*C)%4 != 0:
        return True #Richard wins for non-multiple of 4
    if R*C == 4:
        return True #Richard wins for 4x1 and 2x2
    if R*C == 8:
        return True #Richard wins for 4x2 and 2x4
    return False #Gabriel wins for 4x4
solveD()