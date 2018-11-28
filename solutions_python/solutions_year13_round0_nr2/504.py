fin  = open('B-large.in', 'r')
fout = open('B-large.out', 'w')

def evaluateLawn():
    board = []
    bool_board = []
    l, m = map(int, fin.readline().strip('\n').split())
    for i in range(l):
        row = []
        row = map(int, fin.readline().strip('\n').split())
        board.append(list(row))
        bool_board.append([False] * m) 

    evaluatebrd(board, bool_board)
    for line in bool_board:
        if not all(line):
            break
    else:
        return 'YES'         
    
    board = [[x[i] for x in board] for i in range(m)]
    bool_board = [[x[i] for x in bool_board] for i in range(m)]
    evaluatebrd(board, bool_board)
    for line in bool_board:
        if not all(line):
            return 'NO'
    return 'YES'            
    
def evaluatebrd(board, bool_board):
    for x in range(len(board)):
        maxNum = max(board[x])
        for y in range(len(board[x])):
            if board[x][y] == maxNum: bool_board[x][y] = True
    
if __name__ == '__main__':
    count = fin.readline()
    for j in range(int(count)):
        fout.write('Case #{0}: {1}\n'.format(j + 1, evaluateLawn()))

    fin.close()
    fout.close()
