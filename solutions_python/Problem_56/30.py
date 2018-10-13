def whoWon(board,k):
    winners = []
    for i in xrange(len(board)):
        for j in xrange(len(board)-k+1):
            piece = board[i][j]
            if piece == '.' or piece in winners: continue
            for q in xrange(1,k):
                if piece != board[i][j+q]:
                    break
            else:
                winners.append(piece)
    for i in xrange(len(board)-k+1):
        for j in xrange(len(board)):
            piece = board[i][j]
            if piece == '.' or piece in winners: continue
            for q in xrange(1,k):
                if piece != board[i+q][j]:
                    break
            else:
                winners.append(piece)
    for i in xrange(len(board)-k+1):
        for j in xrange(len(board)-k+1):
            piece = board[i][j]
            if piece == '.' or piece in winners: continue
            for q in xrange(1,k):
                if piece != board[i+q][j+q]:
                    break
            else:
                winners.append(piece)
    for i in xrange(k-1,len(board)):
        for j in xrange(len(board)-k+1):
            piece = board[i][j]
            if piece == '.' or piece in winners: continue
            for q in xrange(1,k):
                if piece != board[i-q][j+q]:
                    break
            else:
                winners.append(piece)
    return winners

def rotate(board):
    newBoard = []
    for i in xrange(len(board)):
        newBoard.append([row[-(i+1)] for row in board])
    return newBoard

def gravity(board):
    newBoard = [[] for _ in xrange(len(board))]
    for j in xrange(len(board)):
        height = 0
        for i in xrange(len(board)):
            if board[i][j] != '.':
                newBoard[height].append(board[i][j])
                height += 1
        for i in xrange(height,len(board)):
            newBoard[i].append('.')
    return newBoard

def printBoard(board):
    for line in reversed(board):
        print ''.join(line)
        
for i in xrange(1,int(raw_input())+1):
    n,k = (int(x) for x in raw_input().split())
    board = []
    for _ in xrange(n):
        board.insert(0,raw_input())
    board = gravity(rotate(board))
    winners = whoWon(board,k)
    if not len(winners): print "Case #%d: Neither" % i
    elif len(winners) == 2: print "Case #%d: Both" % i
    elif winners[0] == "B": print "Case #%d: Blue" % i
    elif winners[0] == "R": print "Case #%d: Red" % i