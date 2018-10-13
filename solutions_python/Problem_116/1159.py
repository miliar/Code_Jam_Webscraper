infile = open('A-large.in','r')
outfile = open('outA.txt','w')

def game_state(board,num):
    players = ['X','O']
    for player in players:
        for i in range(4):
            cur_row = 0
            cur_column = 0
            for j in range(4):
                if board[i][j] == player or board[i][j] == 'T':
                    cur_row += 1
                if board[j][i] == player or board[j][i] == 'T':
                    cur_column += 1
            if cur_row == 4 or cur_column == 4:
                return player + ' won'
        for i in range(1):
            cur_diag1 = 0
            cur_diag2 = 0
            for j in range(4):
                if board[j][j] == player or board[j][j] == 'T':
                    cur_diag1 += 1
                if board[j][3-j] == player or board[j][3-j] == 'T':
                    cur_diag2 += 1
            if cur_diag1 == 4 or cur_diag2 == 4:
                return player + ' won'
    for i in range(4):
        for j in range(4):
            if board[i][j] == '.':
                return "Game has not completed"
    return "Draw"
                
                
                                    
        

num_cases = int(infile.readline())
for i in range(num_cases):
    board = []
    for j in range(4):
        board.append([])
        line = infile.readline()
        for char in line:
            board[j].append(char)
    outfile.write('Case #' + str(i+1) + ': ' + game_state(board,i) + '\n');
    infile.readline()

outfile.close()
infile.close()