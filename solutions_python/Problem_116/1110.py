# board indices 0 to 15

def solve(board):
    for tuple in [(0, 4, 8, 12),
                  (1, 5, 9, 13),
                  (2, 6, 10, 14),
                  (3, 7, 11, 15),
                  (0, 1, 2, 3),
                  (4, 5, 6, 7),
                  (8, 9, 10, 11),
                  (12, 13, 14, 15),
                  (0, 5, 10, 15),
                  (3, 6, 9, 12)]:
        if checkN(board, tuple, 'X'): return "X won"
        if checkN(board, tuple, 'O'): return "O won"
    if '.' in board: return "Game has not completed"
    return "Draw"

#"X won" (the game is over, and X won)
#"O won" (the game is over, and O won)
#"Draw" (the game is over, and it ended in a draw)
#"Game has not completed" (the game is not over yet)

def checkN(board, (a, b, c, d), n):
    return (board[a]=='T' or board[a]==n)\
       and (board[b]=='T' or board[b]==n)\
       and (board[c]=='T' or board[c]==n)\
       and (board[d]=='T' or board[d]==n)

#############################

name = raw_input("'A-small-attempt0.in':\n")

f = open(name+".in", 'r')
g = open(name+".out", 'w')

cases = int(f.readline())

i = 0
while i < cases:
    board = (f.readline() + f.readline() + f.readline() + f.readline())\
        .replace("\n", "")
    
    result = "Case #%d: " % (i+1) + solve(board)
    
    print(result)
    g.write(result + "\n")
    i += 1
    
    f.readline()

f.close()
g.close()

###########################
