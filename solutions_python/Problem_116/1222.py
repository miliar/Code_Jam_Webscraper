def checkwin(board, player):
    ''' checks to see if player has won on board'''
    def winHelper(b):
        for row in b:
            win = True
            for el in row:
                if el not in winLetters:
                    win = False
            if win == True:
                return True
        return False
            
    winLetters = ['T']
    winLetters.append(player)
    #check rows
    winner = winHelper(board)
    #check cols
    winner |= winHelper(map(list, zip(*board)))
    #check diags
    winner |= board[0][0] in winLetters and board[1][1] in winLetters and board[2][2] in winLetters and board[3][3] in winLetters
    winner |= board[0][3] in winLetters and board[1][2] in winLetters and board[2][1] in winLetters and board[3][0] in winLetters
    return winner

def isDraw(board):
    '''assumes checkwin already called'''
    for row in board:
        for el in row:
            if el == '.':
                return 'Game has not completed'
    return 'Draw'

f = open('A-large.in', 'r')

# read first line, number of trials
trials = int(f.readline())

for i in range(trials):
    board = []
    board.append([x for x in f.readline().strip()])
    board.append([x for x in f.readline().strip()])
    board.append([x for x in f.readline().strip()])
    board.append([x for x in f.readline().strip()])
    f.readline()
    if checkwin(board, 'X'):
        status = 'X won'
    elif checkwin(board, 'O'):
        status = 'O won'
    else:
        status = isDraw(board)
    print 'Case #' + str(i + 1) + ': ' + status 
