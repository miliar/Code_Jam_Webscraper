
from sys import stdin

def read_case():
    (rows, columns) = [int(n) for n in stdin.readline().split()]
    matrix = [ [int(n) for n in stdin.readline().split()] for i in range(rows)]
    return (rows, columns, matrix)


def possible(matrix, row_max, col_max):
    for i, row in enumerate(matrix):
        for j, col in enumerate(row):
            if matrix[i][j] < row_max[i] and matrix[i][j] < col_max[j]:
                return False
    return True

cases = int(stdin.readline())

for i in range(1, cases+1):
    (rows, columns, matrix) = read_case()
    #print matrix

    row_max = [max(row) for row in matrix]
    col_max = [max(matrix[i][j] for i in range(rows)) for j in range(columns)]
    #print row_max
    #print col_max

    if possible(matrix, row_max, col_max):
        print "Case #%s: YES" % i
    else:
        print "Case #%s: NO" % i
    