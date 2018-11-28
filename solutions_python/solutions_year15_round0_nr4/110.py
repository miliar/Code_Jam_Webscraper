def solve(X, R, C):
    if R*C % X != 0:
        return 'RICHARD'
    if X >= 7:
        return 'RICHARD'
    elif X == 6:
        if R <= 3 or C <= 3:
            return 'RICHARD'
        if R <= 5 and C <= 5:
            return 'RICHARD'
    elif X == 5:
        if R <= 2 or C <= 2:
            return 'RICHARD'
        if R <= 4 and C <= 4:
            return 'RICHARD'
    elif X == 4:
        if R <= 2 or C <= 2:
            return 'RICHARD'
        if R <= 3 and C <= 3:
            return 'RICHARD'
    elif X == 3:
        if R <= 1 or C <= 1:
            return 'RICHARD'
        if R <= 2 and C <= 2:
            return 'RICHARD'
    return 'GABRIEL'

fin = open('D-small-attempt0.in')

caseNum = int(fin.readline())

for caseNo in range(caseNum):
    tokens = fin.readline().strip().split()
    X = int(tokens[0])
    R = int(tokens[1])
    C = int(tokens[2])
    print('Case #%d: %s' % (caseNo+1, solve(X, R, C)))
fin.close()
