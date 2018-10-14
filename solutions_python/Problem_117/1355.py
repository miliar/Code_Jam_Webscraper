class LAWN_STATUS:
    YES = "YES"
    NO = "NO"

class Problem(object):
    def __init__(self, height, width, lines):
        self.height = height
        self.width = width
        self._matrix = lines
        
    def __getitem__(self, position):
        return self._matrix[position[0]][position[1]*2]
    
    def maxInRow(self, index):
        return max([self[index, j] for j in xrange(self.width)])
    
    def maxInCol(self, index):
        return max([self[i, index] for i in xrange(self.height)])
    
def getSolution(problem):
    for i in xrange(problem.height):
        for j in xrange(problem.width):
            if ((problem[i,j] != problem.maxInRow(i)) and
                (problem[i,j] != problem.maxInCol(j))):
                return LAWN_STATUS.NO
    return LAWN_STATUS.YES

def readProblem(input_file):
    board_lines, board_cols = [int(x) for x in input_file.readline().split(" ")]
    lines = []
    for i in xrange(board_lines):
        lines += [input_file.readline()]
    return Problem(board_lines, board_cols, lines)

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
