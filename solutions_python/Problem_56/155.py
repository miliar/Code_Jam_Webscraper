def rotate (board):
    #b = ["".join(i) for i in board]
    #print "\n".join(b)
    
    for i in range(len(board)):
        for j in range(len(board) - 2, -1, -1):
            if(board[i][j] != '.'):
                c = j
                while c + 1 < len(board) and board[i][c + 1] == '.':
                    c += 1
                if(c != j):
                    board[i][c] = board[i][j]
                    board[i][j] = '.'
    
    #b = ["".join(i) for i in board]
    #print "\n".join(b)
    #print board
    return board

def checkDirection(board, k, i, j, x, y):  
    m, n = i, j
    
    for _ in range(k-1):
        m, n = m + x, n + y
        #print m,n
        if(m < 0 or n < 0 or m >= len(board) or n >= len(board) or 
           board[i][j] != board[m][n]):
            #print "not ok"
            return False
    
    return True
        
def joinK(k, board):
    result = set()
    for i in range(len(board)): 
        for j in range(len(board)):
            box = board[i][j] 
            if(box != '.' and box not in result):
                for x in range(-1, 2):
                    for y in range(-1, 2):
                        if(x == 0 and y == 0): continue
                        #print "tocheck", i,j,x,y
                        if(checkDirection(board, k, i, j, x, y)):                                                       
                            result.add(box)
                            if(len(result) == 2):
                                return "Both"
                            
    if(len(result) == 0):
        return "Neither"
    elif(result.pop() == 'R'):
        return 'Red'    
    return 'Blue'

if __name__ == '__main__':    
    T = int(raw_input())

    for c in range(1, T + 1):   
        N, K = map(int, raw_input().split())
        #print N,K
        board = [list(raw_input()) for _ in range(N)]        
        print "Case #%d: %s" % (c, joinK(K, rotate(board)))
    
    

