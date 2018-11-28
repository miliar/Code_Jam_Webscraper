def check(board, pl):
    for i in range(len(board)):
        b = board[i]
        b = b.replace("T", pl)
        if b.count(pl) == 4:
            return True
    for i in range(len(board)):
        b = ''.join([board[0][i], board[1][i], board[2][i], board[3][i]])
        b = b.replace("T", pl)
        if b.count(pl) == 4:
            return True
    b = ''.join([board[0][0], board[1][1], board[2][2], board[3][3]])
    b = b.replace("T", pl)
    if b.count(pl) == 4:
        return True
    b = ''.join([board[0][3], board[1][2], board[2][1], board[3][0]])
    b = b.replace("T", pl)
    if b.count(pl) == 4:
        return True
    return False

def main():
    file = open("./A-large.in", "r")
    line = file.read()
    lines = line.splitlines()
    T = int(lines[0])
    for i in range(T):
        board = lines[1 + 5*i:5 + 5*i]
        print "Case #{0}:".format(i + 1),
        if check(board, 'X'):
            print "X won"
            continue
        if check(board, 'O'):
            print "O won"
            continue
        if '.' in ''.join(board):
            print "Game has not completed"
        else:
            print "Draw"
        
if __name__ == "__main__":
    main()