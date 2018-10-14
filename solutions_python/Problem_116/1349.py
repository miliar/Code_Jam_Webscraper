def won(board, char):
    b1 = sorted(["T",char,char,char])
    b2 = [char, char, char, char]
    for row in range(4):
        if sorted(board[row]) == b1 or sorted(board[row]) == b2:
            return True
    for col in range(4):
        if sorted([board[i][col] for i in range(4)]) == b1 or \
                sorted([board[i][col] for i in range(4)]) == b2:
            return True
    if sorted([board[0][0],board[1][1],board[2][2],board[3][3]]) == b1 or \
            sorted([board[0][0],board[1][1],board[2][2],board[3][3]]) == b2:
        return True
    if sorted([board[0][3],board[1][2],board[2][1],board[3][0]]) == b1 or \
            sorted([board[0][3],board[1][2],board[2][1],board[3][0]]) == b2:
        return True
    return False

def checkboard(board):
    if won(board, "X"):
        return "X won"
    elif won(board, "O"):
        return "O won"
    elif reduce(lambda a,b: a and b, ['.' not in board[i] for i in range(4)]):
        return "Draw"
    else:
        return "Game has not completed"

fin = open("A-large.in", "r")
fout = open("fdsa.txt", "w")

T = int(fin.readline())
for n in range(T):
    board = []
    for i in range(4):
        board.append(list(fin.readline().strip()))
    fin.readline()
    fout.write("Case #"+str(n+1)+": "+checkboard(board)+"\n")

fin.close()
fout.close()
