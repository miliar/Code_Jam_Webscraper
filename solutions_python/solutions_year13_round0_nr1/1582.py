
def win(letter, board):
    winner = []
    winner.append( letter * 4)
    winner.append((letter * 3) + "T")
    winner.append( "T" + (letter * 3))
    # horizontal check
    for row in board:
        data = "".join(x for x in row)
        if data in winner:
            return True
    # vertical check
    data = ""
    data1 = ""
    data2 = ""
    for i in range(4):
        data1 = data1 + board[i][i]
        data2 = data2 + board[i][3-i]
        data = ""
        for j in range(4):
            data = data + board[j][i]
        if data in winner:
            return True
        # diagonal check
        if data1 in winner:
            return True
        if data2 in winner:
            return True

    return False


def gameOver(board):
    for row in board:
        for item in row:
            if item == ".":
                return False
    return True
    


infile = open("A-small-attempt1.in", "r")

outfile = open("output.txt", "w")

num_C = int(infile.readline().strip())
count = 0

while count < num_C:
    count += 1
    message = "Case #%d: " % count
    board = []
    for i in range(4):
        board.append([])
        board[i] = list(infile.readline().strip())
    if win("X", board):
        message += "X won"
    elif win("O", board):
        message += "O won"
    elif gameOver(board):
        message += "Draw"
    else:
        message += "Game has not completed"
    eat = infile.readline()
    outfile.write(message + "\n")
    
