'''
    Google Code Jam 2013 
    Problem A: Tic-Tac-Toe-Tomek 

    @author: Masood Behabadi
'''

data_file = "data/A-large.in"

def is_winner(s):
    if s.issubset("X") or s.issubset("XT"):
        print "X won"
        return True
    if s.issubset("O") or s.issubset("OT"):
        print "O won"
        return True

def find_winner(board):
    # Rows
    for x in [0, 4, 8, 12]:
        s = set(board[x:x + 4])
        if is_winner(s):
            return True
    # Columns
    for x in [0, 1, 2, 3]:
        s = set([board[i] for i in [x, x + 4, x + 8, x + 12]])
        if is_winner(s):
            return True
    # Diagonal
    s = set([board[i] for i in [0, 5, 10, 15]])
    if is_winner(s):
        return True
    
    s = set([board[i] for i in [3, 6, 9, 12]])
    if is_winner(s):
        return True

if __name__ == '__main__':
    
    f = file(data_file, "r")
    
    ncase = int(f.readline())
    
    for c in xrange(ncase):
        
        print "Case #%s:" % (c + 1),
        
        board = ""
        for n in xrange(5):
            board += f.readline().strip()
        
        if not find_winner(board):
            if "." in board:
                print "Game has not completed"
            else:
                print "Draw"
            
        
        
            
            
    