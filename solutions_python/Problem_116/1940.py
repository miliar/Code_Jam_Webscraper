__author__ = 'cmoravec'
import sys



class Board(object):
    """represents a playing board"""
    _board = [['O', 'X', '.', '.'],
              ['.', 'O', '.', '.'],
              ['X', 'X', 'T', 'X'],
              ['.', 'X', '.', 'O']]

    def __init__(self, newBoard=None):
        if newBoard is not None:
            self._board = newBoard

    def getStatus(self):
        """Returns the current status"""
        oWins = False
        xWins = False
        if self.countChar('.') == 16:
            return 'Game has not completed'
        elif self.countChar('.') == 15:
            return 'Game has not completed'
        if self.findWinner('X'):
            xWins = True
        if self.findWinner('O'):
            oWins = True

        if xWins and oWins:
            return 'Draw'
        elif xWins:
            return 'X won'
        elif oWins:
            return 'O won'

        if not xWins and not oWins and self.countChar('.') == 0:
            return 'Draw'

        return 'Game has not completed'

    def findWinner(self, testChar='X'):
        #only search the first row, since a win has to have a character there
        for i in range(0, 4):
            for j in range(0, 4):
                if self._board[i][j] in [testChar, 'T']:
                    #we could have a winner
                    nList = self.hasNeighbor(i, j, testChar)
                    if len(nList) > 0:
                        #check each neighbor to see if it has a neighbor in the same direction
                        for aNeig in nList:
                            tmp = self.hasNeighborInDirection(aNeig[0], aNeig[1], aNeig[2], testChar)
                            if tmp == 3:
                                return True
        return False


    def hasNeighborInDirection(self, x, y, d, testChar):
        """returns the neighbor that is in the same direction"""
        nList = self.hasNeighbor(x, y, testChar)
        for n in nList:
            if n[2] == d:
                tmp = self.hasNeighborInDirection(n[0], n[1], n[2], testChar)
                if tmp == 0:
                    return 1
                else:
                    return tmp + 1
        if x == 3 or y == 3:
            return 1
        return 0


    def hasNeighbor(self, x, y, testChar):
        """looks to see if any cell next to the specified cell has the same value"""
        neighborList = []
        testList = [testChar, 'T']
        if x + 1 <= 3:
            newX = x + 1
            if self._board[newX][y] in testList:
                neighborList.append([newX, y, 1])
            if y + 1 <= 3:
                if self._board[newX][y + 1] in testList:
                    neighborList.append([newX, y + 1, 2])
            if y - 1 >= 0:
                if self._board[newX][y - 1] in testList:
                    neighborList.append([newX, y - 1, 3])
        if x - 1 >= 0:
            newX = x - 1
            if self._board[newX][y] in testList:
                neighborList.append([newX, y, 4])
            if y + 1 <= 3:
                if self._board[newX][y + 1] in testList:
                    neighborList.append([newX, y + 1, 5])
            if y - 1 >= 0:
                if self._board[newX][y - 1] in testList:
                    neighborList.append([newX, y - 1, 6])
        if y + 1 <= 3:
            if self._board[x][y + 1] in testList:
                neighborList.append([x, y + 1, 7])
        if y - 1 >= 0:
            if self._board[x][y - 1] in testList:
                neighborList.append([x, y - 1, 8])

        return neighborList



    def countChar(self, inputChar='.'):
        charCount = 0
        for i in range(0, 4):
            for j in range(0, 4):
                if self._board[i][j] == inputChar:
                    charCount += 1
        return charCount


def readFile(pathToFile):
    boardList = []
    with open(pathToFile) as f:
        rows = f.readlines()
    boardCount = int(rows[0].strip())
    for i in range(1, boardCount * 4 + (boardCount - 1), 5):
        board = []
        for j in range(0, 4):
            newRow = []
            for k in range(0, 4):
                newRow.append(rows[i + j][k])
            board.append(newRow)
        boardList.append(board)
    return boardList



def main():
    bCount = 1
    f = open(sys.argv[2], "w")
    for aBoard in readFile(sys.argv[1]):
        b = Board(aBoard)
        printString = "Case #{}: {}".format(bCount, b.getStatus())
        f.write(printString + "\n")
        print printString
        bCount += 1
    f.close()


if __name__ == '__main__':
    main()
