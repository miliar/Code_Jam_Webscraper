import sys
import psyco

def proxy(function):
    return psyco.proxy(function)

class Case:
    def __init__(self, s, caseNum):
        self.caseNum = caseNum
        self.r, self.conn = [int(x) for x in s.read().split(" ")]
        self.c = self.r
        self.board = s.readList(self.r)

    @proxy
    def solve(self):
        self.rotated = [['.' for unused_row in xrange(self.r)] for unused_col in xrange(self.c)]
        for row_iter in xrange(self.r):
            row = self.r - row_iter - 1
            target_col = row_iter
            target_row = self.c - 1 
            for col_iter in xrange(self.c):
                col = self.c - col_iter - 1
                if self.board[row][col] == '.':
                    continue
                self.rotated[target_row][target_col] = self.board[row][col]
                target_row -= 1
        red = self.is_connected(self.rotated, "R", self.conn)
        blue = self.is_connected(self.rotated, "B", self.conn)
        if red & blue:
            return "Both"
        if red:
            return "Red"
        if blue:
            return "Blue"
        return "Neither"
    
    @proxy
    def is_connected(self, board, symbol, length):
        for row in xrange(self.r):
            for col in xrange(self.c):
                if board[row][col] != symbol:
                    continue
                for rowdir, coldir in [(0, 1), (1, -1), (1, 0), (1, 1)]:
                    match = True
                    for i in xrange(1, length):
                        nextrow = row + rowdir * i
                        nextcol = col + coldir * i
                        if nextrow < 0 or nextrow >= self.r or nextcol < 0 or nextcol >= self.r:
                            match = False
                            break
                        if board[nextrow][nextcol] != symbol:
                            match = False
                            break
                    if match:
                        return True
        return False
    
    def __repr__(self):
        return "Problem A Case %d" % self.caseNum

class Contents:
    def __init__(self, f):
        self.data = [line.strip() for line in f]
        self.i = 0

    def read(self):
        return self.readList(1)[0]

    def readList(self, len):
        result = self.data[self.i : self.i + len]
        self.i += len
        return result

def run():
    f = file(sys.argv[1])
    s = Contents(f)
    numCases = int(s.read())
    
    for caseNum in range(numCases):
        case = Case(s, caseNum)
        print "Case #%d: %s" % (caseNum + 1, case.solve())
        sys.stdout.flush()
        
if __name__ == "__main__":
    run()