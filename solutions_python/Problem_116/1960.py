# tictactoetomek1.py

def determine_winner(board):
   
    # count horizontal num X/O and T
    row = 0
    h = 0
    while row < 4:
        if board[h:h+4].count('X') + board[h:h+4].count('T') == 4:
            return "X won"
        if board[h:h+4].count('O') + board[h:h+4].count('T') == 4:
            return "O won"
        row = row + 1
        h = h + 4    
        
    # count vertical num X/O and T
    col = 0
    while col < 4:
        if board[0+col].count('X') + board[0+col].count('T') + \
           board[4+col].count('X') + board[4+col].count('T') + \
           board[8+col].count('X') + board[8+col].count('T') + \
           board[12+col].count('X') + board[12+col].count('T') == 4:
            return "X won"
        if board[0+col].count('O') + board[0+col].count('T') + \
           board[4+col].count('O') + board[4+col].count('T') + \
           board[8+col].count('O') + board[8+col].count('T') + \
           board[12+col].count('O') + board[12+col].count('T') == 4:
            return "O won"
        col = col + 1
        
    # count diagonal num X/O and T    
    if board[0].count('X') + board[0].count('T') + \
       board[5].count('X') + board[5].count('T') + \
       board[10].count('X') + board[10].count('T') + \
       board[15].count('X') + board[15].count('T') == 4:
        return "X won"
    if board[3].count('X') + board[3].count('T') + \
       board[6].count('X') + board[6].count('T') + \
       board[9].count('X') + board[9].count('T') + \
       board[12].count('X') + board[12].count('T') == 4:
        return "X won"
    if board[0].count('O') + board[0].count('T') + \
       board[5].count('O') + board[5].count('T') + \
       board[10].count('O') + board[10].count('T') + \
       board[15].count('O') + board[15].count('T') == 4:
        return "O won"
    if board[3].count('O') + board[3].count('T') + \
       board[6].count('O') + board[6].count('T') + \
       board[9].count('O') + board[9].count('T') + \
       board[12].count('O') + board[12].count('T') == 4:
        return "O won"

    if board.count('.') >= 1:
        return "Game has not completed"

    if board.count('X') + board.count('O') + board.count('T') == 16:
        return "Draw"

# main

fin = open("A-large.in", 'r')
fout = open("A-large.out", 'w')

T = int(fin.readline())

i = 1
for game in range(0,T):
    gameboard = []
    for row in range(0,4):
        line = fin.readline()
        for col in range(0,4):
            gameboard.append(line[col])
    # skip blank line
    blankline = fin.readline()
    outcome = determine_winner(gameboard)
    fout.write("Case #{}: {}\n".format(str(i), str(outcome)))
    i = i + 1
    
fin.close()
fout.close()
