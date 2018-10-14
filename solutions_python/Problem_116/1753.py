class Game:
    def __init__(self):
        self.winner = ''
        self.row = []
        self.drawable = True

    def addRow(self, source):
        if source.find(".") > -1:
            self.drawable = False
        self.row.append(Row(source))

    def getCell(self, x, y):
        return self.row[x].col[y]

    def isWinning(self, point1, point2, point3, point4):

        cell1 = self.getCell(point1[0], point1[1])
        cell2 = self.getCell(point2[0], point2[1])
        cell3 = self.getCell(point3[0], point3[1])
        cell4 = self.getCell(point4[0], point4[1])
        
        compare = ""
        if cell1 != "T" and cell1 != ".":
            compare = cell1
        elif cell2 != "T" and cell2 != ".":
            compare = cell2
        elif cell3 != "T" and cell3 != ".":
            compare = cell3
        elif cell4 != "T" and cell4 != ".":
            compare = cell4
        else:
            return False

        if cell1 != compare and cell1 != "T":
            return False
        elif cell2 != compare and cell2 != "T":
            return False
        elif cell3 != compare and cell3 != "T":
            return False
        elif cell4 != compare and cell4 != "T":
            return False
        else:
            self.winner = compare
            return True

    def isWon(self):
        if self.isWinning([0, 0], [0, 1], [0, 2], [0, 3]):
            return True
        elif self.isWinning([1, 0], [1, 1], [1, 2], [1, 3]):
            return True
        elif self.isWinning([2, 0], [2, 1], [2, 2], [2, 3]):
            return True
        elif self.isWinning([3, 0], [3, 1], [3, 2], [3, 3]):
            return True
        elif self.isWinning([0, 0], [1, 0], [2, 0], [3, 0]):
            return True
        elif self.isWinning([0, 1], [1, 1], [2, 1], [3, 1]):
            return True
        elif self.isWinning([0, 2], [1, 2], [2, 2], [3, 2]):
            return True
        elif self.isWinning([0, 3], [1, 3], [2, 3], [3, 3]):
            return True
        elif self.isWinning([0, 0], [1, 1], [2, 2], [3, 3]):
            return True
        elif self.isWinning([0, 3], [1, 2], [2, 1], [3, 0]):
            return True
        else:
            return False

    def getStatus(self):
        if self.isWon():
            if self.winner == "X":
                return "X won"
            elif self.winner == "O":
                return "O won"
            else:
                raise Exception('Unknown winner')
        else:
            if self.drawable:
                return "Draw"
            else:
                return "Game has not completed"

class Row:
    def __init__(self, source):
        self.col = []
        self.col.append(source[0])
        self.col.append(source[1])
        self.col.append(source[2])
        self.col.append(source[3])

def getCases():
    contents = []
    with open('A-large.in', 'r') as f:
        contents = f.read().split("\n")

    test_count = contents[0]
    test_cases = []
    
    limit = len(contents)
    
    for i in range(1, limit + 1, 5):
        game = Game()
        game.addRow(contents[i])
        game.addRow(contents[i + 1])
        game.addRow(contents[i + 2])
        game.addRow(contents[i + 3])
        test_cases.append(game)

    return test_count, test_cases

def createOutput():
    f = open('output.txt', 'w')
    test_count, test_cases = getCases()
    for i in range(0, int(test_count)):
        f.write("Case #" + str(i + 1) + ": " + test_cases[i].getStatus() + "\n")
    
    f.close()
