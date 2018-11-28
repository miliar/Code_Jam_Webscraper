from sys import stdin
from collections import namedtuple

Lawn = namedtuple('Lawn', ['grid', 'rows', 'cols'])

def row(lawn, y):
    for x in xrange(lawn.cols):
        yield lawn.grid[y][x]

def col(lawn, x):
    for y in xrange(lawn.rows):
        yield lawn.grid[y][x]

def read_lawn():
    [rows, cols] = [int(s) for s in stdin.readline().strip().split()]

    grid = []
    for line in xrange(rows):
        line_strs = [int(h) for h in stdin.readline().strip().split()]
        grid.append(line_strs)

    return Lawn(grid, rows, cols)

def is_cuttable(lawn):
    row_max = [max(row(lawn, y)) for y in xrange(lawn.rows)]
    col_max = [max(col(lawn, x)) for x in xrange(lawn.cols)]

    for x in xrange(lawn.cols):
        for y in xrange(lawn.rows):
            if lawn.grid[y][x] < row_max[y] and lawn.grid[y][x] < col_max[x]:
                return False
    return True

def do():
    cases = int(stdin.readline().strip())
    for x in xrange(cases):
        lawn = read_lawn()
        answer = "YES" if is_cuttable(lawn) else "NO"
        print "Case #%d: %s" %(x + 1, answer)

if __name__ == '__main__':
    do()

