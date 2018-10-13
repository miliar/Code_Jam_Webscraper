def isWinner(board, p):
    
    for x in range(4):
        matchCount = 0
        for y in range(4):
            if board[x][y] == p or board[x][y] == 'T':
                matchCount += 1

        if matchCount == 4:
            return True

        matchCount = 0
        for y in range(4):
            if board[y][x] == p or board[y][x] == 'T':
                matchCount += 1

        if matchCount == 4:
            return True

    matchCount = 0
    for x in range(4):
        if board[x][x] == p or board[x][x] == 'T':
            matchCount += 1

    if matchCount == 4:
        return True

    matchCount = 0
    for x in range(4):
        if board[x][3-x] == p or board[x][3-x] == 'T':
            matchCount += 1

    if matchCount == 4:
        return True

    return False
            
def isComplete(board):
    for x in range(4):
        for y in range(4):
            if board[x][y] == '.':
                return False
    return True

inData = [str(line.strip()) for line in open('tick.in') if line.strip() != ""]

N = int(inData.pop(0))

for caseNum in range(1, 1+N):
    board = []
    for x in range(4):
        board.append(inData.pop(0))

    if isWinner(board, 'X'):
        print "Case #%s: X won" % caseNum
        continue
        
    if isWinner(board, 'O'):
        print "Case #%s: O won" % caseNum
        continue

    if isComplete(board):
        print "Case #%s: Draw" % caseNum
        continue
        
    print "Case #%s: Game has not completed" % caseNum

    


