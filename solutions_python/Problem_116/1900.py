def open_file (filename='input.txt'):
    fin = open(filename, 'r')
    lines = fin.read().split('\n')
    if lines[-1] == '':
        lines = lines[:-1]
    fin.close()

    return lines

def parse_file(lines):
    board_count = int(lines[0])
    boards = []
    for i in range(board_count):
        board = []
        for j in range(4):
            board.append(lines[i*5+j+1])
        boards.append(board)
        
    return boards

def get_rows(board):
    return board

def get_cols(board):
    cols = []
    for i in range(4):
        col = ''
        for row in board:
            col += row[i]
        cols.append(col)
    return cols

def get_diags(board):
    diag = ''
    diag2 = ''
    for i in range(4):
        diag += board[i][i]
        diag2 += board[i][-(i+1)]

    return [diag,diag2]

def get_winner(board):
    x_win = ['XXXX','XXXT','XXTX','XTXX','TXXX']
    o_win = ['OOOO','OOOT','OOTO','OTOO','TOOO']

    rows = board + get_cols(board) + get_diags(board)
    for row in rows:
        if row in x_win:
            return 'X won'
        if row in o_win:
            return 'O won'

    for row in board:
        if '.' in row:
            return 'Game has not completed'
    return 'Draw'

if __name__ == "__main__":
    fout = open('output.txt', 'w')
    for i, board in enumerate(parse_file(open_file('input.txt'))):
        fout.write('Case #' + str(i+1) + ': ' + get_winner(board) + '\n')
    fout.close()
    print 'Done'
