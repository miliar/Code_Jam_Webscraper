def horCheck (board, char):
    for line in board:
        if char == line[0] == line[1] == line[2] == line[3]:
            return True
    return False

def diagCheck(board, char):
    if char == board[0][0] == board[1][1] == board[2][2] == board[3][3]:
        return True
    if char == board[0][3] == board[1][2] == board[2][1] == board[3][0]:
        return True
    return False

def findOne(board, char):
    for line in board:
        for sec in line:
            if sec == char:
                return True
    return False
    
def check (board):
    #replace T with X and O in xwin and owin
    xwin = []
    owin = []
    for line in board:      #cycle through each line
        xline = []
        oline = []
        for char in line:   #cycle through each char
            if char == 'T':
                xline.append('X')
                oline.append('O')
            else:
                xline.append(char)
                oline.append(char)
        xwin.append(xline)
        owin.append(oline)
    #check for matches
    if horCheck(xwin, 'X') or horCheck(zip(*xwin), 'X') or diagCheck(xwin, 'X'):
        return "X won"
    if horCheck(owin, 'O') or horCheck(zip(*owin), 'O') or diagCheck(owin, 'O'):
        return "O won"
    #draw or not complete
    if findOne(board, '.'):
        return "Game has not completed"
    else:
        return "Draw"
            

def main():
    f = open("A-large.in", 'r')
    f2 = open("output.txt", 'w')

    n = int(f.readline())
    for i in xrange(n):
        board = []
        for j in xrange(4):
            board.append(list(f.readline())[:4])
        f.readline()    #blank line in file
        f2.write("Case #" + str(i+1) + ": " + check(board) + "\n")
    
    f.close();
    f2.close();
    
if __name__ == "__main__":
    main()
