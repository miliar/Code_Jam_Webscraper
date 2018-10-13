PLUS = "+"
CROSS = "x"
TRENDYO = "o"
EMPTY = "."
class Grid():
    def __init__(self, r, c):
        self.R = r
        self.C = c
        self.grid = []
        for i in range(self.R):
            self.grid.append([])
            for j in range(self.C):
                self.grid[i].append(None)
        self.letters = []

    def add(self, r,c, l):
        self.grid[r][c] = l
        if(l != "?"):
            self.letters.append(Letter(r,c,l, self))

    def checkCol(self, let, col, s, e):
        if col >= len(self.grid[0]) or col < 0:
            return False

        for i in range(s,e+1):
            if self.grid[i][col] != let and self.grid[i][col] != "?":
                return False
        for i in range(s,e+1):
            self.grid[i][col] = let

        return True

    def checkRow(self, let, row, s, e):
        if row >= len(self.grid) or row < 0:
            return False

        # print(s)
        # print(e)
        # print(row)
        for i in range(s,e+1):
            if self.grid[row][i] != let and self.grid[row][i] != "?":
                return False
        for i in range(s,e+1):
            self.grid[row][i] = let
        return True

    def run(self):
        for l in self.letters:
            while(l.up()):
                pass
        for l in self.letters:
            while(l.left()):
                pass
        for l in self.letters:
            while(l.down()):
                pass
        for l in self.letters:
            while(l.right()):
                pass
        for i in range(len(self.grid)):
            for j in range(len(self.grid[0])):
                if self.grid[i][j] == "?":
                    self.letters = self.letters[-1:] + self.letters[:-1]
                    self.run()

    def print(self):
        for i in range(len(self.grid)):
            for j in range(len(self.grid[0])):
                print(self.grid[i][j],end="")
            print()
        # for i in range(len(self.letters)):
        #     print(self.letters[i].l)

class Letter():
    def __init__(self, r, c, l, grid):
        self.start_R = r
        self.start_C = c
        self.end_R = r
        self.end_C = c
        self.l = l
        self.grid=grid
    def right(self):
        if self.grid.checkCol(self.l, self.end_C+1, self.start_R, self.end_R):
            self.end_C += 1
            return True
        else:
            return False

    def left(self):
        if self.grid.checkCol(self.l, self.start_C - 1, self.start_R, self.end_R):
            self.start_C -= 1
            return True
        else:
            return False

    def down(self):
        if self.grid.checkRow(self.l, self.end_R + 1, self.start_C, self.end_C):
            self.end_R += 1
            return True
        else:
            return False
    def up(self):
        if self.grid.checkRow(self.l, self.start_R - 1, self.start_C, self.end_C):
            self.start_R -= 1
            return True
        else:
            return False






t = int(input())  # read a line with a single integer
for i in range(1, t + 1):
    R, C = [int(s) for s in input().split(" ")]  # read a list of integers, 2 in this case
    g = Grid(R, C)
    for j in range(R):
        cols = list(input())
        # print(cols)
        for k in range(C):
            l = cols[k]
            g.add(j, k, l)
            # print("Adding" + l)
            # g.print()
            # print()

    g.run()
    print("Case #{}:".format(i))
    g.print()
    # check out .format's specification for more formatting options

