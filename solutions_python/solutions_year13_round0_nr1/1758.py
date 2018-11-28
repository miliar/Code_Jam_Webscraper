def checkRowWon(row):
    winner = 0
    for c in row:
        if c == '.':
            return False
        elif c == 'X':
            if winner == 0 :
                winner = 1
            elif winner == 2 :
                return False
        elif c == 'O':
            if winner == 0 :
                winner = 2
            elif winner == 1 :
                return False
        elif c == 'T':
            continue
    if winner == 1 :
        print "X won"
    elif winner == 2 :
        print "O won "
    return True

import sys
f = open(sys.argv[1], 'r')

numOfTest = int(f.readline())

for i in range(1, numOfTest + 1) :
    print "Case #" + str(i) + ":",
    
    # read test case
    test = []
    for j in range(4) :
        test.append(f.readline())
    
    # check test case for row
    checkFinished = False
    for j in range(4) :
        if checkRowWon(test[j]) :
            checkFinished = True
            break
    if checkFinished :
        f.readline() # empty line
        continue
    
    # check test case for column
    for j in range(4) :
        if checkRowWon(test[0][j] + test[1][j] + test[2][j] + test[3][j]) :
            checkFinished = True
            break
    if checkFinished :
        f.readline() # empty line
        continue
    
    # check test case for diagonal
    diag = ""
    for j in range(4) :
        diag = diag + test[j][j]
    if checkRowWon(diag) :
        f.readline()
        continue
    diag = ""
    for j in range(4) :
        diag = diag + test[j][3 - j]
    if checkRowWon(diag) :
        f.readline()
        continue
    
    # check test case for draw
    for j in range(16) :
        if test[j % 4][j / 4] == '.' :
            print "Game has not completed"
            break
    else :
        print "Draw"
    f.readline()
