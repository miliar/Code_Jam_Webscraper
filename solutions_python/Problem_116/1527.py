class GAME_STATUS:
    X_WON = "X won"
    O_WON = "O won"
    DRAW = "Draw"
    NOT_OVER = "Game has not completed"
class GAME_CELL:
    X = "X"
    O = "O"
    EMPTY = "."
    T = "T"

class Problem(object):
    def __init__(self, lines):
        self._matrix = lines
        
    def isCell(self, x, y, verify):
        return (self._matrix[x][y] == verify) or (self._matrix[x][y] == GAME_CELL.T)
    
    def __getitem__(self, position):
        return self._matrix[position[0]][position[1]]
    
    @property
    def isFinished(self):
        for i in xrange(4):
            for j in xrange(4):
                if (self[i,j] == GAME_CELL.EMPTY):
                    return False
        return True
    
def getWinState(cell):
    if (cell == "X"):
        return GAME_STATUS.X_WON
    if (cell == "O"):
        return GAME_STATUS.O_WON
    
def getSolution(problem):
    for i in xrange(4):
        current = problem[0, i]
        if ((current != GAME_CELL.EMPTY) and 
            (problem.isCell(1, i, current)) and 
            (problem.isCell(2, i, current)) and 
            (problem.isCell(3, i, current))):
            return getWinState(current)
        
        current = problem[i, 0]
        if ((current != GAME_CELL.EMPTY) and 
            (problem.isCell(i, 1, current)) and 
            (problem.isCell(i, 2, current)) and 
            (problem.isCell(i, 3, current))):
            return getWinState(current)
    
    current = problem[0, 0]
    if ((current != GAME_CELL.EMPTY) and 
        (problem.isCell(1, 1, current)) and 
        (problem.isCell(2, 2, current)) and 
        (problem.isCell(3, 3, current))):
        return getWinState(current)
    
    current = problem[0, 3]
    if ((current != GAME_CELL.EMPTY) and 
        (problem.isCell(1, 2, current)) and 
        (problem.isCell(2, 1, current)) and 
        (problem.isCell(3, 0, current))):
        return getWinState(current)
    
    if (problem.isFinished):
        return GAME_STATUS.DRAW
    else:
        return GAME_STATUS.NOT_OVER

def readProblem(input_file):
    lines = []
    for i in xrange(4):
        lines += [input_file.readline()]
    input_file.readline() #empty line
    return Problem(lines)

def executeFile(file_path):
    input_file = file(file_path, "r")
    output_file = file(file_path + ".out", "w")
    count = int(input_file.readline());
    index = 0
    while (index < count):
        problem = readProblem(input_file)
        sol = getSolution(problem)
        output_file.write("Case #" + str(index + 1) + ": " + sol + "\n")
        index = index + 1
    output_file.close()

def main():
    import sys
    if (len(sys.argv) < 2):
        print "Wrong number of arguments!\n" + \
              "Arguments: file_path"
        return
    for i in xrange(len(sys.argv) - 1):
        executeFile(sys.argv[i + 1])
    
if (__name__ == "__main__"):
    main()
    
    