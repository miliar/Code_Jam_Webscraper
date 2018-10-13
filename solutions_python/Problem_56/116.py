import sys

def print_board(board, N):
    
    for i in range(N):
        print board[i]

def join_k(board, N, K):
    
    #print '\nN=%s, k=%s, start' % (N, K)
    #print_board(board, N)
    
    #print '\nrotated'
    rotated_board = rotate(board, N)
    #print_board(rotated_board, N)

    #print '\ngravity'
    apply_gravity(rotated_board, N)
    #print_board(rotated_board, N)
    
    winners = find_winner(rotated_board, N, K)
    if len(winners) == 2:
        return 'Both'
    elif len(winners) == 1 and winners[0] == 'R':
        return 'Red'
    elif len(winners) == 1 and winners[0] == 'B':
        return 'Blue'
    else:
        return 'Neither'

def rotate(board, N):
    
    rotated_board = []
    
    for i in range(N):
        rotated_board.append(['.'] * N)
        
    for i in range(N):
        for j in range(N):
            rotated_board[j][N-i-1] = board[i][j]
        
    return rotated_board

def apply_gravity(board, N):
    
    for j in range(N):
        new_col = ''
        for i in range(N-1, -1, -1):
            if board[i][j] != '.':
                new_col += board[i][j]
        for i in range(N-1, -1, -1):
            board[i][j] = '.'
        new_col = list(new_col)
        for i in range(N-1, -1, -1):
            if new_col:
                board[i][j] = new_col.pop(0)
            else:
                break

def find_winner(board, N, K):
    
    winners = []
    
    for i in range(N):
        for j in range(N):
            res = check_spot(board, N, K, i, j)
            if res and res not in winners:
                winners.append(res)
                if len(winners) == 2:
                    break
        if len(winners) == 2:
            break
    
    return winners

def check_spot(board, N, K, i, j):
    
    player = board[i][j]
    if player == '.':
        return None
    
    # check horizontal
    for j_delta in range(K):
        if j+j_delta >= N or board[i][j+j_delta] != player:
            break
    else:
        #print 'found horiz winner %s at %s, %s', player, i, j
        return player

    # check vertical
    for i_delta in range(K):
        if i+i_delta >= N or board[i+i_delta][j] != player:
            break
    else:
        #print 'found vert winner %s at %s, %s', player, i, j
        return player
    
    # top-left to bottom-right diag
    for delta in range(K):
        if i+delta >= N or j+delta >= N or board[i+delta][j+delta] != player:
            break
    else:
        #print 'found tl-br winner %s at %s, %s', player, i, j
        return player
    
    # bottom-left to top-right diag
    for delta in range(K):
        #print 'checking %s, %s for player %s, value %s' % (i-delta, j+delta, player, board[i-delta][j+delta])
        if i-delta < 0 or j+delta >= N or board[i-delta][j+delta] != player:
            break
    else:
        #print 'found bl-tr winner %s with K=%s at %s, %s after delta %s' % (player, K, i, j, delta)
        return player
    
    return None
    

if __name__ == '__main__':
    
    ntests = int(sys.stdin.readline())
    for i in range(1, ntests+1):
        N, K = map(int, sys.stdin.readline().split())
        board = []
        for j in range(N):
            board.append(list(sys.stdin.readline().strip()))
        #print 'new board', board
        ans = join_k(board, N, K)
        print 'Case #%s: %s' %  (i, ans)
