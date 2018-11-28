class RR(object):

    X = 0
    O = 1
    Undec = 2
    Draw = 3

    lookup = dict([(X, 'X won'), (O, 'O won'), (Draw, 'Draw'), (Undec, 'Game has not completed')])

    @classmethod
    def string(cls, item):
        return cls.lookup[item]


        

class Board(object):
    """docstring for Board"""
    def __init__(self, lines):
        super(Board, self).__init__()
        self.lines = lines
        self.n = len(lines)

    def get(self, i , j):
        return self.lines[i][j]


class Problem1(object):
    """docstring for Problem1"""
    def __init__(self, board):
        super(Problem1, self).__init__()
        self.board = board

    def solve_row(self, i):
        return self.solve_pairs([(i,j) for j in range(0,self.board.n)])

    def solve_col(self, j):
        return self.solve_pairs([(i,j) for i in range(0,self.board.n)])

    def solve_l_diag(self):
        return self.solve_pairs([(i,i) for i in range(0, self.board.n)])

    def solve_r_diag(self):
        return self.solve_pairs([(self.board.n -1 - i,i) for i in range(0, self.board.n)])



    def solve_pairs(self, pairs):
        sln = RR.Undec
        for i,j in pairs:
            val = self.board.get(i,j)
            if ord(val) is ord('.'):
                return RR.Undec
            if sln is RR.Draw:
                continue
            if ord(val) is ord('T'):
                continue
            if ord(val) is ord('X'):
                if sln is RR.Undec or sln is RR.X:
                    sln = RR.X
                    continue
                else:
                    sln = RR.Draw
            if ord(val) is ord('O'):
                if sln is RR.Undec or sln is RR.O:
                    sln = RR.O
                    continue
                else:
                    sln = RR.Draw
        return sln



        

    def solve(self):
        draw = True
        for i in range(0, self.board.n):
            sln = self.solve_row(i)
            if sln is RR.X or sln is RR.O:
                return sln
            if sln is RR.Undec:
                draw = False
            sln = self.solve_col(i)
            if sln is RR.X or sln is RR.O:
                return sln
            if sln is RR.Undec:
                draw = False            
        l =  self.solve_l_diag()
        if (l is RR.X) or (l is RR.O):
            return l
        if l is RR.Undec:
            draw = False
        r =  self.solve_r_diag()
        if r is RR.X or r is RR.O:
            return r
        if r is RR.Undec:
            draw = False
        if draw:
            return RR.Draw
        return RR.Undec


def main():
    with open('A-large.in','r') as fn:
        n = int(fn.readline()[:-1])
        for i in range(1,n+1):
            mat = []
            for _ in range(0,4):
                line = fn.readline()
                if line[-1] is '\n':
                    line = line[:-1]
                mat.append(line)
            try:
                fn.readline()
            except:
                pass
            print 'Case #{0}: {1}'.format(i, RR.string(Problem1(Board(mat)).solve()))
    

if __name__ == '__main__':
    main()

