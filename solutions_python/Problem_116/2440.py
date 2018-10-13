import sys

def check_rows(board, player):
    for row in board:
      if (row.count(player) == 3 and row.count('T')) or row.count(player) == 4:
        return True
    return False

def check_cols(board, player):
    cols = zip(*board)
    return check_rows(cols, player)

def check_diag(board, player):
    main_diagonal = [board[i][i] for i in xrange(4)]
    anti_diagonal = [board[len(board[i])-1-i][i] for i in xrange(4)]
    return check_rows([main_diagonal, anti_diagonal], player)

def check_completed(board):
    dots = sum(row.count('.') for row in board)
    return False if dots > 0 else True

def print_board(board):
    for row in board:
      for col in row:
        print col,
      print 

def main():
    test_case = int(sys.stdin.readline())
    for i in xrange(1, test_case+1):
        board = [list(sys.stdin.readline())[:-1] for _ in xrange(4)]
        for symbol in 'XO':
            rows = check_rows(board, symbol) 
            cols = check_cols(board, symbol)
            diag = check_diag(board, symbol)
            if rows or cols or diag:
                print('Case #%d: %s won' %  (i, symbol))
                break 
        else:
            if not check_completed(board):
                print('Case #%d: Game has not completed' % (i))
            else:
                print('Case #%d: Draw' % (i))
        sys.stdin.readline()
       

if __name__=='__main__':
    main()
