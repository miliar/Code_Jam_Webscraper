import sys
from operator import attrgetter

class Lawn:
    def __init__(self, lines):
        self.squaresDict = {}
        for r, l in enumerate(lines):
            self.squaresDict[r] = {}
            for c, h in enumerate(l.strip().split(' ')):
                self.squaresDict[int(r)][int(c)] = Square(int(r), int(c), int(h))
        
        self.rows = len(lines)
        self.cols = len(lines[0].strip().split(' '))

    def outcome(self):
        remainingRows = set(range(self.rows))
        remainingCols = set(range(self.cols))
        
        #sorted by height, ascending
        for s in sorted([x for row in self.squaresDict.values() for x in row.values()], key=attrgetter('height')):
            
            # if this is largest eq, this row or column is OK
            rowOK = s.height >= max([self.squaresDict[s.row][c].height for c in range(self.cols)])
            colOK = s.height >= max([self.squaresDict[r][s.col].height for r in range(self.rows)])

            if ((not rowOK) and (not colOK)):
                return "NO"
            
            if rowOK:
                remainingRows.discard(s.row)
            if colOK:
                remainingCols.discard(s.col)

            if ((not remainingRows) and (not remainingCols)):
                return "YES"


class Square:
    def __init__(self, row, col, height):
        self.row = row
        self.col = col
        self.height = height


fp = open(sys.argv[1], "r")

lines = fp.readlines()

fpOut = open("outputB.txt", "w")

numCases = int(lines[0].strip())
ptr = 1
for c in range(1, numCases+1):
    N = int(lines[ptr].strip().split(' ')[0])
    l = Lawn(lines[ptr+1:ptr+1+N])
    ptr += N + 1
    
    result = "Case #%d: %s\n"%(c, l.outcome())

    fpOut.write(result)
    
fp.close()
fpOut.close()
