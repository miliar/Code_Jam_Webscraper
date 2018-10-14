import sys


index_map = [0] * 256
index_map[ord('X')] = 0
index_map[ord('O')] = 1
index_map[ord('T')] = 2
index_map[ord('.')] = 3

def judge_game_by_row_col(row_or_col):
    if row_or_col[index_map[ord('T')]] == 1:
        if row_or_col[index_map[ord('X')]] == 3:
            return "X won"
        elif row_or_col[index_map[ord('O')]] == 3:
            return "O won"
    else:
        if row_or_col[index_map[ord('X')]] == 4:
            return "X won"
        elif row_or_col[index_map[ord('O')]] == 4:
            return "O won"
    return None
            

def judge_game(board):    
    col_result = [[0]*4,[0]*4,[0]*4,[0]*4]
    row_result = [0] * 4
    left_edge = [0] * 4
    right_edge = [0] * 4
    has_dot = False    
    for row in xrange(0,4):        
        for col in xrange(0,4):
            c = board[row][col]
            i = index_map[ord(c)]
            row_result[i] += 1
            col_result[col][i] += 1
            if row == col:
                left_edge[i] += 1
            if col == 3 - row:
                right_edge[i] += 1                        
            if c == '.':
                has_dot = True                    
        game_result = judge_game_by_row_col(row_result)                
        if game_result is not None:
            return game_result 
        row_result = [0] * 4            
    for col in col_result:
        game_result = judge_game_by_row_col(col)                
        if game_result is not None:
            return game_result
            
    game_result = judge_game_by_row_col(left_edge)                
    if game_result is not None:
        return game_result
        
    game_result = judge_game_by_row_col(right_edge)                
    if game_result is not None:
        return game_result 
                   
    if has_dot:
        return "Game has not completed"
    else:
        return "Draw"
        
            

num_case = int(sys.stdin.readline())

for case_id in xrange(1,num_case+1):
    board = []    
    for i in xrange(0,4):
        board.append(sys.stdin.readline().strip())
    sys.stdin.readline()
    print "Case #%s: %s" % (case_id, judge_game(board))

            
            
            
    