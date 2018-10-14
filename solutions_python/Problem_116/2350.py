import sys

def ReadFile(filename):
    file = open(filename)
    n = int(file.readline())
    for case in range(1,n+1):
        board = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
        for row in range(0,4):
            newrow = file.readline()
            for i in range(0,4):
                board[row][i] = newrow[i]
        
        print("Case #" + str(case) + ": " + TicTacToeTomec(board))
        file.readline()


def TicTacToeTomec(board):


    TPosition = CheckTPosition(board)

    if CheckRows(board, TPosition) == "X won" or CheckColumns(board, TPosition) == "X won" or CheckDiagonal(board, TPosition) == "X won" or CheckOppositeDiagonal(board, TPosition) == "X won":
        return "X won"
    elif CheckRows(board, TPosition) == "O won" or CheckColumns(board, TPosition) == "O won" or CheckDiagonal(board, TPosition) == "O won" or CheckOppositeDiagonal(board, TPosition) == "O won":
        return "O won"
    GameCompleted = True
    for i in range(0,4):
        for j in range(0,4):
            if board[i][j] == ".":
                GameCompleted = False
    if GameCompleted == False:
        return "Game has not completed"
    else:
        return "Draw"



def CheckTPosition(board):
    TPosition = [-1,-1]
    for i in range(0,4):
        for j in range(0,4):
            if board[i][j] =="T":
                TPosition = [i,j]
    return TPosition


def CheckRows(board, TPosition):
    if TPosition[1] != -1:
        for row in range(0,4):
            XRow = True
            YRow = True
            for column in range(0,4):
                if TPosition != [row, column] and board[row][column] != "X":
                    XRow = False
                if TPosition != [row, column] and board[row][column] != "O":
                    YRow = False
            if XRow == True:
                return "X won"
            if YRow == True:
                return "O won"
    else:
        for row in range(0,4):
            if board[row][0] == board[row][1] == board[row][2] == board[row][3] == "X":
                return "X won"
            if board[row][0] == board[row][1] == board[row][2] == board[row][3] == "O":
                return "O won"
    return "No Row"

def CheckColumns(board, TPosition):
    if TPosition != [-1,-1]:
        for column in range(0,4):
            XColumn = True
            YColumn = True
            for row in range(0,4):
                if TPosition != [row, column] and board[row][column] != "X":
                    XColumn = False
                if TPosition != [row, column] and board[row][column] != "O":
                    YColumn = False
            if XColumn == True:
                return "X won"
            if YColumn == True:
                return "O won"
    else:
        for column in range(0,4):
            if board[0][column] == board[1][column] == board[2][column] == board[3][column] == "X":
                return "X won"
            if board[0][column] == board[1][column] == board[2][column] == board[3][column] == "O":
                return "O won"
    return "No Column"

def CheckDiagonal(board, TPosition):
    if TPosition[0] == TPosition[1] != -1:
        XDiagonal = True
        YDiagonal = True
        for i in range(0,4):
            if TPosition != [i,i] and board[i][i] != "X":
                XDiagonal = False
            if TPosition != [i,i] and board[i][i] != "O":
                YDiagonal = False           
        if XDiagonal == True:
            return "X won"
        if YDiagonal == True:
            return "O won"        
    else:
        if board[0][0] == board[1][1] == board[2][2] == board[3][3] == "X":
            return "X won"
        if board[0][0] == board[1][1] == board[2][2] == board[3][3] == "O":
            return "O won"
    return "No Diagonal"


def CheckOppositeDiagonal(board, TPosition):
    if TPosition[0] == 3 - TPosition[1] != -1:
        XDiagonal = True
        YDiagonal = True
        for i in range(0,4):
            if TPosition != [i,3 - i] and board[i][3 - i] != "X":
                XDiagonal = False
            if TPosition != [i,3 - i] and board[i][3 - i] != "O":
                YDiagonal = False           
        if XDiagonal == True:
            return "X won"
        if YDiagonal == True:
            return "O won"        
    else:
        if board[0][3] == board[1][2] == board[2][1] == board[3][0] == "X":
            return "X won"
        if board[0][3] == board[1][2] == board[2][1] == board[3][0] == "O":
            return "O won"
    return "No Opposite Diagonal"


if __name__ == '__main__':
    ReadFile(sys.argv[1])
