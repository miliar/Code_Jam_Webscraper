def processBoard(board):
    # Test for row win
    for row in board:

        if row.count('X') == 4:
            return 'X won'
        elif row.count('O') == 4:
            return 'O won'
        elif row.count('X') == 3 and row.count('T') == 1:
            return 'X won'
        elif row.count('O') == 3 and row.count('T') == 1:
            return 'O won'

    # Test for column win
    ## X
    for j in range(0, 4):
        count = 0
        
        for k in range(0, 4):
            if board[k][j] == 'X' or board[k][j] == 'T':
                count += 1
            else:
                k = 4

        if count == 4:
            return 'X won'

    ## O
    for j in range(0, 4):
        count = 0
        
        for k in range(0, 4):
            if board[k][j] == 'O' or board[k][j] == 'T':
                count += 1
            else:
                k = 4

        if count == 4:
            return 'O won'

    # Test for diagional win
    ## X
    count = 0
    for i in range(0, 4):
        if board[i][i] != 'X' and board[i][i] != 'T':
            i = 4
        else:
            count += 1
            
    if count == 4:
        return 'X won'

    ## O
    count = 0
    for i in range(0, 4):
        if board[i][i] != 'O' and  board[i][i] != 'T':
            i = 4
        else:
            count += 1

    if count == 4:
        return 'O won'

    ### Backwards

    ## X
    count = 0
    for i in range(0, 4):
        if board[i][3-i] != 'X' and board[i][3-i] != 'T':
            i = 4
        else:
            count += 1
            
    if count == 4:
        return 'X won'

    ## O
    count = 0
    for i in range(0, 4):
        if board[i][3-i] != 'O' and  board[i][3-i] != 'T':
            i = 4
        else:
            count += 1

    if count == 4:
        return 'O won'

    return 'Draw'


i = open('A-large.in', 'r+')
o = open('output.txt', 'w+')

text = i.readlines()
num = int(text[0])
del[text[0]]

for i in range(0, num):
    board = []

    
    # Read in board
    for k in range(0, 4):
        board.append(text[0])
        del[text[0]]

    if i != num-1:
        del[text[0]] # Remove white space

    winner = processBoard(board)

    if winner == 'Draw':
        for row in board:
            for c in row:
                if c == '.':
                    winner = 'Game has not completed'

    o.write('Case #' + str(i+1) + ": " + winner + "\n" )

print('STOP')
o.close()
    
