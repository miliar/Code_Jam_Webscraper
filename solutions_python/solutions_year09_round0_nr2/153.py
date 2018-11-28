debug = False

def main(inputFilename):
    f = open(inputFilename)
    testCases = getArgs(f)
    if debug:
        printArgs(testCases)
    solveTestCases(testCases)

def getArgs(f):
    testCases = []
    T = int(f.readline())
    for i in range(T):
        (Hstr, Wstr) = f.readline().split()
        H = int(Hstr)
        W = int(Wstr)
        map = Map(H, W)
        for row in range(map.rows):
            cols = f.readline().split()
            for (col, elevationStr) in enumerate(cols):
                elevation = int(elevationStr)
                cell = Cell(row, col, elevation)
                map.addCell(cell)
        testCase = TestCase(map)
        testCases.append(testCase)
    return (testCases)

def printArgs(testCases):
    print("T (number of maps): {0}".format(len(testCases)))
    print
    for testCase in testCases:
        map = testCase.map
        print("H (rows): {0}".format(map.rows))
        print("W (columns): {0}".format(map.cols))
        for row in map.cellMatrix:
            for cell in row:
                print cell.elevation,
            print
        print

def solveTestCases(testCases):
    for (testCaseNumber, testCase) in enumerate(testCases):
        map = testCase.map
        createBasins(map)
        labelBasins(map)
    printSolutions(testCases)

def printSolutions(testCases):
    for (testCaseNumber, testCase) in enumerate(testCases):
        print("Case #{0}:".format(1 + testCaseNumber))
        printMapNames(testCase.map)

def printMapNames(map):
    for row in map.cellMatrix:
        for cell in row:
            print cell.basin.name,
        print
            
def createBasins(map):
    for row in map.cellMatrix:
        for cell in row:
            createBasinFromCell(map, cell)

def createBasinFromCell(map, cell):
    if cell.basin != None:
        return cell.basin
    else:
        neighbors = map.getCellNeighbors(cell)
        lowestNeighbor = cell
        for neighbor in neighbors:
            if neighbor.elevation < lowestNeighbor.elevation:
                lowestNeighbor = neighbor
        if lowestNeighbor == cell:
            cell.basin = Basin()
            return cell.basin
        else:
            cell.basin = createBasinFromCell(map, lowestNeighbor)
            return cell.basin

def labelBasins(map):
    nameIndex = ord("a")
    for row in map.cellMatrix:
        for cell in row:
            basin = cell.basin
            if basin.name == None:
                basin.name = chr(nameIndex)
                nameIndex += 1


class Cell:
    def __init__(self, row, col, elevation):
        self.row = row
        self.col = col
        self.elevation = elevation
        self.basin = None

    def setBasin(self, basin):
        self.basin = basin
        basin.addCell(self)

class Basin:
    def __init__(self):
        self.cells = []
        self.name = None

    def addCell(self, cell):
        self.cells.append(cell)
        cell.basin = self

class Map:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.cells = []
        self.initializeCellMatrix()

    def initializeCellMatrix(self):
        self.cellMatrix = []
        for row in range(self.rows):
            self.cellMatrix.append([])
            for col in range(self.cols):
                self.cellMatrix[row].append(None)

    def getCell(self, row, col):
        return self.cellMatrix[row][col]

    def addCell(self, cell):
        self.cells.append(cell)
        self.cellMatrix[cell.row][cell.col] = cell

    def getCellNeighbors(self, cell):
        neighbors = []
        row = cell.row
        col = cell.col
        if row > 0:
            neighbors.append(self.getCell(row - 1, col))
        if col > 0:
            neighbors.append(self.getCell(row, col - 1))
        if col < self.cols - 1:
            neighbors.append(self.getCell(row, col + 1))
        if row < self.rows - 1:
            neighbors.append(self.getCell(row + 1, col))
        return neighbors

class TestCase:
    def __init__(self, map):
        self.map = map;

if (__name__ == "__main__"):
    import sys
    inputFilename = sys.argv[1]
    main(inputFilename)
