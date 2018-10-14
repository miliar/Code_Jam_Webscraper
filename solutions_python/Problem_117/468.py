from itertools import product

def main(matrix, case):
    row_max = []
    col_max = []
    for r in matrix:
        row_max.append(max(r))
        for i, j in enumerate(r):
            if len(col_max) <= i:
                col_max.append(0)
            if col_max[i] < j:
                col_max[i] = j

    all = product(range(len(row_max)), range(len(col_max)))
    for a in all:
        i = a[0]
        j = a[1]
        if matrix[i][j] < row_max[i] and matrix[i][j] < col_max[j]:
            print "Case #" + str(case) + ": NO"
            return

    print "Case #" + str(case) + ": YES"



f = open('input.txt', 'r')
num_samples = int(f.readline().strip())

for i in xrange(num_samples):
    rows, cols = map(int, f.readline().strip().split(' '))
    matrix = []
    for j in xrange(rows):
        row = map(int, f.readline().strip().split(' '))
        matrix.append(row)

    main(matrix, i+1)
