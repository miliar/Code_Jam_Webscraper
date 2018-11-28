import os
import sys

sys.stdin = open(os.path.join(os.path.dirname(__file__), 'B-small-attempt0.in'))
sys.stdout = open('out2.txt', 'wb')

cases = int(raw_input())


class cube(object):
    def __init__(self, val, row, col):
        super(cube, self).__init__()
        self.v = val
        self.row = row
        self.col = col
        self.ignore = False

        self.r = None
        self.l = None
        self.t = None
        self.b = None

    def cut(self, method=None):
        global rows
        global matrix

        cell = None
        while True:
            m = self.min()
            if m[0] == 101:
                return True
            cell = matrix[m[1][0]][m[1][1]]

            if cell.isHorz():
                for c in range(cols):
                    if matrix[cell.row][c].isVert():
                        for r in range(rows):
                            matrix[r][c].ignore = True
                    matrix[cell.row][c].ignore = True

            elif cell.isVert():
                for r in range(rows):
                    if matrix[r][cell.col].isHorz():
                        for c in range(cols):
                            matrix[r][c].ignore = True

                    matrix[r][cell.col].ignore = True
            else:
                return False

    def isVert(self):
        t = self.t
        while t:
            if not t.ignore:
                if t.v != self.v:
                    return False
            t = t.t

        b = self.b
        while b:
            if not b.ignore:
                if b.v != self.v:
                    return False
            b = b.b

        return True

    def isHorz(self):
        l = self.l
        while l:
            if not l.ignore:
                if l.v != self.v: return False
            l = l.l
        r = self.r
        while r:
            if not r.ignore:
                if r.v != self.v: return False
            r = r.r
        return True

    def poz(self):
        return self.row, self.col

    def min(self):
        m = self.v if not self.ignore else 101
        poz = self.poz()
        if self.r:
            rv = self.r.min()
            if rv[0] < m:
                m = rv[0]
                poz = rv[1]
        if self.b:
            bv = self.b.min()
            if bv[0] < m:
                m = bv[0]
                poz = bv[1]

        return m, poz


def prepare(mat, r, c):
    for row in range(r):
        for col in range(c):
            if row > 0:
                mat[row][col].t = mat[row-1][col]
            if col > 0:
                mat[row][col].l = mat[row][col-1]
            if row < r - 1:
                mat[row][col].b = mat[row+1][col]
            if col < c - 1:
                mat[row][col].r = mat[row][col+1]


def solve(mat, r, c):
    global case
    rez = mat[0][0].cut()
    print 'Case #%d: %s' % (case + 1, 'YES' if rez else 'NO')


for case in range(cases):
    rows, cols = raw_input().split(' ')
    rows = int(rows)
    cols = int(cols)

    matrix = []
    for i in range(rows):
        line = raw_input().split(' ')
        row = []
        for e in range(cols):
            c = cube(int(line[e]), i, e)
            row.append(c)
        matrix.append(row)

    prepare(matrix, rows, cols)
    solve(matrix, rows, cols)

