import sys

input_count = int(sys.stdin.readline())


def occupy_by(board, marks):
    #Horizontal 
    for j in range(0,4):
        if board[j][0] in marks and board[j][1] in marks and board[j][2] in marks and board[j][3] in marks :
            return True
    
    for j in range(0,4):
        if board[0][j] in marks and board[1][j] in marks and board[2][j] in marks and board[3][j] in marks :
            return True
    
    if board[0][0] in marks and board[1][1] in marks and board[2][2] in marks and board[3][3] in marks :
        return True
    
    if board[0][3] in marks and board[1][2] in marks and board[2][1] in marks and board[3][0] in marks :
        return True


for i in range(1,input_count+1):

    winner = None
    board = []

    for j in range(0,4):
        
        line = sys.stdin.readline().strip()
        if len(line) == 0 : 
            line = sys.stdin.readline().strip()
        
        board_line = []
        for c in line :
            board_line.append(c)
        
        board.append(board_line)
    
    marks = set(['X','T'])
    if occupy_by(board, marks):
        print "Case #{0}: X won".format(i)
        continue
    
    marks = set(['O','T'])
    if occupy_by(board, marks):
        print "Case #{0}: O won".format(i)
        continue
        
    draw = True
    for j in range(0,4):
        if '.' in board[j]:
            draw = False
            
    if draw:
        print "Case #{0}: Draw".format(i)
    else:
        print "Case #{0}: Game has not completed".format(i)


