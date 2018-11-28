class Solver(object):
    def __init__(self, mat):
        self.mat = mat
        self.blacklist = {'?'}

    def solve(self):
        solved = False
        while not solved:
            # scan the table for the first non blacklisted letter
            row = 0
            col = 0
            found = False
            for c in range(len(self.mat[0])):
                if found:
                    break
                for r in range(len(self.mat)):
                    if self.mat[r][c] not in self.blacklist:
                        row = r
                        col = c
                        found = True
                        break
            # make the rectangle as tall as possible
            top = row
            bottom = row
            for r in range(row-1, -1, -1):
                if self.mat[r][col] == '?':
                    top = r
                else:
                    break
            for r in range(row+1, len(self.mat)):
                if self.mat[r][col] == '?':
                    bottom = r
                else:
                    break
            # make the rectangle as wide as possible
            left = col
            right = col
            for c in range(col-1, -1, -1):
                empty = True
                for r in range(top, bottom + 1):
                    if self.mat[r][c] != '?':
                        empty = False
                        break
                if empty:
                    left = c
                else:
                    break
            for c in range(col+1, len(self.mat[0])):
                empty = True
                for r in range(top, bottom + 1):
                    if self.mat[r][c] != '?':
                        empty = False
                        break
                if empty:
                    right = c
                else:
                    break
            # fill in the rectangle
            for r in range(top, bottom + 1):
                for c in range(left, right + 1):
                    self.mat[r][c] = self.mat[row][col]
            # blacklist the char
            self.blacklist.add(self.mat[row][col])
            # check if solved
            solved = True
            for r in range(len(self.mat)):
                for c in range(len(self.mat[r])):
                    if self.mat[r][c] == '?':
                        solved = False
        return self.mat

T = int(input())
for i in range(T):
    rows, cols = tuple(int(s) for s in input().split(' '))
    mat = []
    for r in range(rows):
        mat.append(list(input()))
    solver = Solver(mat)
    print('Case #%s:' % (i+1))
    smat = solver.solve()
    for row in smat:
        print(''.join(row))
