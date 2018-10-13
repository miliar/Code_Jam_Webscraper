with open('in.txt') as f:
    lines = f.readlines()

n = int(lines[0])

output = []

def check_win(player, cells):
    win = True
    for cell in cells:
        if cell != player and cell != "T":
            win = False
            break
    return win

def check_blanks(board):
    for row in board:
        for cell in row:
            if cell == ".":
                return True
    return False

for i in xrange(0,n):
    board = [line.rstrip() for line in lines[5*i+1:5*i+5]]
    X_won = False
    O_won = False

    # rows
    for q in xrange(0,4):
        cells = board[q]
        X_won = X_won | check_win("X", cells)
        O_won = O_won | check_win("O", cells)
    
    # columns
    for c in xrange(0,4):
        cells = [board[r][c] for r in xrange(0,4)]
        X_won = X_won | check_win("X", cells)
        O_won = O_won | check_win("O", cells)

    # diagonals
    diag1 = [board[0][0], board[1][1], board[2][2], board[3][3]]
    diag2 = [board[3][0], board[2][1], board[1][2], board[0][3]]
    X_won = X_won | check_win("X", diag1) | check_win("X", diag2)
    O_won = O_won | check_win("O", diag1) | check_win("O", diag2)

    text = "Case #" + str(i+1) + ": "
    if X_won and not O_won:
        text += "X won"
    elif O_won and not X_won:
        text += "O won"
    elif X_won and O_won:
        text += "Draw"
    elif check_blanks(board):
        text += "Game has not completed"
    else:
        text += "Draw"

    print text

    output.append(text)

with open('out.txt', 'w') as f:
    f.write("\n".join(output)+"\n") 
