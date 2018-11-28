
def read_input(filename):
    data = []
    with file(filename, 'rt') as f:
        for line in f:
            data.append(line)
        
    line_num = int(data[0].strip())
	
    boards = []
    curr_line = 1
    for _ in xrange(line_num):
        curr_board = []
        for _ in xrange(4):
            curr_board.append([data[curr_line][i] for i in xrange(4)])
            curr_line += 1
        curr_line += 1
        boards.append(curr_board)

    print boards
    return boards

def get_board_state(board):
        if (any(all(i in ['X', 'T'] for i in line) for line in board) or
            any(all(line[i] in ['X', 'T'] for line in board) for i in xrange(4)) or
            all(board[i][i] in ['X', 'T'] for i in xrange(4)) or
            all(board[i][3-i] in ['X', 'T'] for i in xrange(4))):
           return 'X won'
        elif (any(all(i in ['O', 'T'] for i in line) for line in board) or
              any(all(line[i] in ['O', 'T'] for line in board) for i in xrange(4)) or
              all(board[i][i] in ['O', 'T'] for i in xrange(4)) or
              all(board[i][3-i] in ['O', 'T'] for i in xrange(4))):
           return 'O won'
        elif all(all(i in ['X', 'O', 'T'] for i in line) for line in board):
           return 'Draw'
        else:
           return 'Game has not completed'

def get_state(boards):
    res = []
    for board in boards:
        res.append(get_board_state(board))
        
    print res
    return res

def create_output(res):
    with file('output1.txt', 'wt') as f:
        for (i, line) in enumerate(res):
            print >> f, 'Case #%d: %s' % (i + 1, line) 
            
def main():
    import sys
    data = read_input(sys.argv[1])
    res = get_state(data)
    create_output(res)

if __name__ == "__main__":
    main()