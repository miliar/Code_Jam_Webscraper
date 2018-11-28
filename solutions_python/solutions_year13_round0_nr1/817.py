'''
Created on Apr 12, 2013

@author: herman
'''


infile = open("small_input.txt","r")
outfile = open("small_output.txt","w")

trials = int(infile.readline())

def game_status(board):
    def check_rows(board):
        for i in xrange(4):
            x_wins = True
            o_wins = True
            for j in xrange(4):
                x_wins = x_wins and (board[i][j] == 'X' or board[i][j] == 'T')
                o_wins = o_wins and (board[i][j] == 'O' or board[i][j] == 'T')
            if x_wins:
                return 'X'
            elif o_wins:
                return 'O'
        return '.'
    def check_columns(board):
        for j in xrange(4):
            x_wins = True
            o_wins = True
            for i in xrange(4):
                x_wins = x_wins and (board[i][j] == 'X' or board[i][j] == 'T')
                o_wins = o_wins and (board[i][j] == 'O' or board[i][j] == 'T')
            if x_wins:
                return 'X'
            elif o_wins:
                return 'O'
        return '.'
    def check_diag(board):
        x_wins = True
        o_wins = True
        for i in xrange(4):
            x_wins = x_wins and (board[i][i] == 'X' or board[i][i] == 'T')
            o_wins = o_wins and (board[i][i] == 'O' or board[i][i] == 'T')
        if x_wins:
            return 'X'
        elif o_wins:
            return 'O'
        
        x_wins = True
        o_wins = True
        for i in xrange(4):
            x_wins = x_wins and (board[i][-(i+1)] == 'X' or board[i][-(i+1)] == 'T')
            o_wins = o_wins and (board[i][-(i+1)] == 'O' or board[i][-(i+1)] == 'T')
        if x_wins:
            return 'X'
        elif o_wins:
            return 'O'
        else:
            return '.'
    if (check_rows(board) == 'X' or check_columns(board) == 'X' or check_diag(board) == 'X'):
        return 'X won'
    elif (check_rows(board) == 'O' or check_columns(board) == 'O' or check_diag(board) == 'O'):
        return 'O won'
    else:
        total_pieces = sum([sum([p != '.' for p in row]) for row in board])
        if total_pieces == 16:
            return 'Draw'
        else:
            return 'Game has not completed'

for i in xrange(trials):
    board = [['' for x in xrange(4)] for y in xrange(4)]
    for j in xrange(4):
        line = infile.readline().strip()
        while len(line) == 0:
            line = infile.readline().strip()
        for k in xrange(4):
            board[j][k] = line[k]
    
    result = game_status(board)
    s = "Case #%d: %s\n" % (i+1,result)
    outfile.write(s)
    print s
    
infile.close()
outfile.close()