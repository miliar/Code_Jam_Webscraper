import sys, math

    
num_cases = int(sys.stdin.readline())


def get_iters(board, max_x, max_y):
    
    empty = True
    
    new_max_x = 0
    new_max_y = 0

    for i in xrange(max_x+1, 0, -1):
        for j in xrange(max_y+1, 0, -1):
            if board[i][j] == 1:
                if board[i-1][j] == 0 and board[i][j-1] == 0:
                    board[i][j] = 0
                else:
                    empty = False
                    new_max_x = max(i, new_max_x)
                    new_max_y = max(j, new_max_y)
            else:
                if board[i-1][j] == 1 and board[i][j-1] == 1:
                    board[i][j] = 1
                    empty = False
                    new_max_x = max(i, new_max_x)
                    new_max_y = max(j, new_max_y)
            
    if empty:
        return 1
    else:
        return 1 + get_iters(board, new_max_x, new_max_y)

for k in xrange(num_cases):
    
    R = int(sys.stdin.readline())
    
    board = []
    for _ in xrange(500):
        board.append([0] * 500)
    
    max_x = 0
    max_y = 0
    for _ in xrange(R):
        x1, y1, x2, y2 = [int(e) for e in sys.stdin.readline().split()]
        for i in xrange(x1, x2+1):
            for j in xrange(y1, y2+1):
                board[i][j] = 1
                max_x = max(i, max_x)
                max_y = max(j, max_y)
    
    
    print "Case #%s: %s" % (k+1, get_iters(board, max_x, max_y))
    k += 1
