example   = 'example.txt'
smallData = 'A-small-attempt1.in'
largeData = 'A-large.in'
output    = 'out.txt'

boardSize = 4

def scanALine(line):
    X, O, T, empty = 0, 0, 0, 0
    for elm in line:
        if elm == '.':
            empty += 1
        elif elm == 'X':
            X += 1
        elif elm == 'O':
            O += 1
        elif elm == 'T':
            T += 1
        else:
            raise Exception('Invalid Character')

    return X, O, T, empty

def evaLineStatus(paras):
    X, O, T, empty = paras
    
    if X == boardSize or (X == boardSize - 1 and T == 1):
        return 'X won'
    elif O == boardSize or (O == boardSize - 1 and T == 1):
        return 'O won'
    else:
        return 'Not sure'

with open(largeData, 'r') as f, open(output, 'w') as outFile:
    t = int(f.readline())
    print 'T =', t

    for caseNum in xrange(t):
        print 'Case #{}'.format(caseNum + 1)
        
        board = []
        for i in xrange(boardSize):
            row = list(f.readline().rstrip('\n'))
##            print 'a row:', row

            board.append(row)

        f.readline() # jump the empty line

##        print 'board:'
##        for row in board:
##            print row

        # evaluate result
        gameOver = False
        
        boardStatistic = (0, 0, 0, 0) # (X, O, T, .)

        # scan row
        for row in board:
            scanResult = scanALine(row)
##            print 'scanResult:', scanResult

            # statistc only once, avoid duplication
            import operator
            boardStatistic = tuple(map(operator.add, boardStatistic, scanResult))
##            print 'boardStatistic:', boardStatistic

            lineStatus = evaLineStatus(scanResult)
##            print 'lineStatus:', lineStatus
            
            if lineStatus != 'Not sure':
                gameOver = True
                print lineStatus
                print
                out = 'Case #{0}: {1}\n'.format(caseNum + 1, lineStatus)
                outFile.write(out)
                break

        if gameOver:
            continue

        # scan column
        for colNum in xrange(boardSize):
            column = []
            for rowNum in xrange(boardSize):
                column.append(board[rowNum][colNum])

##            print 'A column:', column

            colStatus = evaLineStatus(scanALine(column))
##            print 'colStatus:', colStatus

            if colStatus != 'Not sure':
                gameOver = True
                print colStatus
                print
                out = 'Case #{0}: {1}\n'.format(caseNum + 1, colStatus)
                outFile.write(out)                
                break

        if gameOver:
            continue

        # scan diagonal
        topleft, topright = (0, 0), (0, boardSize - 1)
        offsets = ( (1, 1), (1, -1) )
        for pos, offset in zip((topleft, topright), offsets):
##            print 'pos, offset =', pos, offset

            diagonal = []
            for diaNum in xrange(boardSize):
                x = pos[0] + offset[0] * diaNum
                y = pos[1] + offset[1] * diaNum
##                print 'x, y =', x, y
                diagonal.append(board[x][y])

##            print 'a diagonal:', diagonal

            diaStatus = evaLineStatus(scanALine(diagonal))
##            print 'diaStatus:', diaStatus

            if diaStatus != 'Not sure':
                gameOver = True
                print diaStatus
                print
                out = 'Case #{0}: {1}\n'.format(caseNum + 1, diaStatus)
                outFile.write(out)                
                break

        if gameOver:
            continue

        # evaluate Not completed or Draw
        if boardStatistic[3] >0:
            print 'Game has not completed'
            out = 'Case #{0}: {1}\n'.format(caseNum + 1, 'Game has not completed')
            outFile.write(out)            
        else:
            print 'Draw'
            out = 'Case #{0}: {1}\n'.format(caseNum + 1, 'Draw')
            outFile.write(out)             

        print 'boardStatistic:', boardStatistic
        print



            
