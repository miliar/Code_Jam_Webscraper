
fin = open("A-large.in","r")
fout = open("output.txt","w")
i = fin.readline()

boards = fin.read()
boards = boards.split("\n\n")

i = 0
for board in boards:
    result = 0
    if board == "":
        result = 1
        exit
    
    i = i + 1
    board = board.split("\n")
    #check if any rows filled
    print board
    if result == 0:
        row = 0
        while row < 4:
            print row
            if(board[row][0] == board[row][1] or board[row][0] == 'T' or board[row][1] == 'T'):
                if(board[row][0] == 'X' or board[row][0] == 'O'):
                    player = board[row][0]
                elif(board[row][1] == 'X' or board[row][1] == 'O'):
                    player = board[row][1]
                else:
                    player = '.'
                if(board[row][2] == player or board[row][2] == 'T') and player != '.':
                    if(board[row][3] == player  or board[row][3] == 'T'):
                        fout.write("Case #"+str(i) +": "+ player + " won\n")
                        result = 1
            row = row + 1
    if result == 0:
        row = 0
        while row < 4:
            if(board[0][row] == board[1][row] or board[0][row] == 'T' or board[1][row] == 'T'):
                if(board[0][row] == 'X' or board[0][row] == 'O'):
                    player = board[0][row]
                elif(board[1][row] == 'X' or board[1][row] == 'O'):
                    player = board[1][row]
                else:
                    player = '.'
                if(board[2][row] == player or board[2][row] == 'T') and player != '.':
                    if(board[3][row] == player  or board[3][row] == 'T'):
                        fout.write("Case #"+str(i) +": "+ player + " won\n")
                        result = 1
            row = row + 1
    if result == 0:
        if(board[0][0] == board[1][1] or board[0][0] == 'T' or board[1][1] == 'T'):
            if(board[0][0] == 'X' or board[0][0] == 'O'):
                player = board[0][0]
            elif(board[1][1] == 'X' or board[1][1] == 'O'):
                player = board[1][1]
            else:
                player = '.'
            if(board[2][2] == player or board[2][2] == 'T') and player != '.':
                if(board[3][3] == player  or board[3][3] == 'T'):
                    fout.write("Case #"+str(i) +": "+ player + " won\n")
                    result = 1

    if result == 0:
        if(board[3][0] == board[2][1] or board[3][0] == 'T' or board[2][1] == 'T'):
            if(board[3][0] == 'X' or board[3][0] == 'O'):
                player = board[3][0]
            elif(board[2][1] == 'X' or board[2][1] == 'O'):
                player = board[2][1]
            else:
                player = '.'
            if(board[1][2] == player or board[1][2] == 'T') and player != '.':
                if(board[0][3] == player  or board[0][3] == 'T'):
                    fout.write("Case #"+str(i) +": "+ player + " won\n")
                    result = 1
    if result == 0:
        for row in board:
            if '.' in row and result == 0:
                fout.write("Case #"+str(i) +": Game has not completed\n")
                result = 1
    
    if result == 0:
        fout.write("Case #"+str(i) +": Draw\n")
fin.close()
fout.close()
