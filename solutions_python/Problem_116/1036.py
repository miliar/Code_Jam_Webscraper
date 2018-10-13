import sys

dim = 4

def diagonals(board):
    global dim
    blttr = [None]*dim
    tltbr = [None]*dim
    for i in range(dim):
        tltbr[i] = board[i][i]
        blttr[i] = board[dim-1-i][i]    
    return blttr,tltbr

def line_check(line):
    global dim
    winner = None
    incomplete = True
    x_count = 0
    o_count = 0
    for c in line:
        if c == 'X':
            x_count += 1
        elif c == 'O':
            o_count += 1
        elif c == 'T':
            o_count += 1
            x_count += 1
        else:
            return incomplete, winner
    incomplete = False
    if x_count == dim:
        winner = 'X'
    elif o_count == dim:
        winner = 'O'
    return incomplete, winner

def board_result(board):
    global dim
    winner = None
    incomplete = False
    for i in range(dim):
        line = board[i]
        incomplete_line, winner = line_check(board[i])
        if winner:
            break
        incomplete = incomplete or incomplete_line
    if not winner:
        for i in range(dim):
            line = [row[i] for row in board]
            incomplete_line, winner = line_check(line)
            if winner:
                break
            incomplete = incomplete or incomplete_line
    if not winner:
        blttr,tltbr = diagonals(board)
        for line in [blttr,tltbr]:
            incomplete_line, winner = line_check(line)
            if winner:
                break
            incomplete = incomplete or incomplete_line
    if winner:
        return "%s won" % (winner)
    elif incomplete:
        return "Game has not completed"
    else:
        return "Draw"

def main():
    global dim
    filename = sys.argv[1]
    file = open(filename, 'r')
    input_size = int(file.readline())
    board = [None]*dim
    for i in range(input_size):
        for j in range(dim):
            line = file.readline()
            board[j] = list(line[:dim])
        print "Case #%d: %s" % (i+1,  board_result(board))
        file.readline()

if __name__ == '__main__':
    main()