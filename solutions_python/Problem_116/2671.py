import sys
class Board:
    board = []
    def __init__(self, board):
        self.board = board

    def printBoard(self):
        print self.board

    def isUnfinished(self):
        for x in xrange(0, 4):
            for y in xrange(0, 4):
                if self.board[x][y] == ".":
                    return True
        return False

    def isVerticalWin(self, symbol):
        for column in xrange(0, 4):
            isVerticalLine = True
            for line in xrange(0, 4): 
                if(self.board[line][column] != symbol and self.board[line][column] != "T"):
                    isVerticalLine = False
            if isVerticalLine:
                return True
        return False

    def isHorizontalWin(self, symbol):
        for line in xrange(0, 4):
            isHorizontalLine = True
            for column in xrange(0, 4): 
                if(self.board[line][column] != symbol and self.board[line][column] != "T"):
                    isHorizontalLine = False
            if isHorizontalLine:
                return True
        return False

    def isDiagonalWin(self, symbol):
        isDiagonalLine = True
        for x in xrange(0, 4):
            if(self.board[x][x] != symbol and self.board[x][x] != "T"):
                isDiagonalLine = False
        if isDiagonalLine:
            return True
        isDiagonalLine = True
        for y in xrange(3, -1, -1):
            if(self.board[y][3 - y] != symbol and self.board[y][3 - y] != "T"):
                isDiagonalLine = False
        if isDiagonalLine:
            return True
        return False    
                

    def isXWon(self): 
        if(self.isHorizontalWin("X")):
            return True
        if(self.isVerticalWin("X")):
            return True
        if(self.isDiagonalWin("X")):
            return True
        return False

    def isYWon(self): 
        if(self.isHorizontalWin("O")):
            return True
        if(self.isVerticalWin("O")):
            return True
        if(self.isDiagonalWin("O")):
            return True
        return False

#MAIN
boards = []
__file__ = sys.argv[1]
f = open(__file__, 'r')
numberOfTestCases = f.readline()
for board in xrange(0, int(numberOfTestCases)):
    lines = []
    for line in xrange(0 ,4):
        lines.append(list(f.readline()))
    boards.append(Board(lines))
    f.readline()

for board in xrange(0, int(numberOfTestCases)):
    if boards[board].isXWon():  
        print "Case #" + str(board + 1) + ": X won"
    elif boards[board].isYWon():
        print "Case #" + str(board + 1) + ": O won"
    elif boards[board].isUnfinished():
        print "Case #" + str(board + 1) + ": Game has not completed"
    else:
        print "Case #" + str(board + 1) + ": Draw"
