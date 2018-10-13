import sys

line = sys.stdin.readline()
NUMBER = int(line.strip())

for case in range(0, NUMBER):
    line = sys.stdin.readline().strip().split()
    line = [int(i) for i in line]
    HORIZONTAL = line[0]
    VERTICAL = line[1]
    matrix = [] 
    for row in range(0, HORIZONTAL):
        line = sys.stdin.readline().strip().split()
        line = [int(i) for i in line]
        matrix.append(line)
    while True:
        i = 0
        while i < len(matrix):
            if not matrix[i]:
                del matrix[i]
            else:
                i += 1
        if not matrix:
            break
        height_minimum = 100
        row_minimum = 0
        column_minimun = 0
        row_size = len(matrix)
        column_size = len(matrix[0])
        for row in range(0, row_size):
            for column in range(0, column_size):
                if height_minimum > matrix[row][column]:
                    height_minimum = matrix[row][column]
                    row_minimum = row
                    column_minimun = column
        row_cut = (sum(1 for value in matrix[row_minimum] if value == height_minimum) == column_size)
        column_cut = (sum(1 for row in matrix if row[column_minimun] == height_minimum) == row_size)
        if (not row_cut) and (not column_cut):
            print 'Case #%d: %s' % (case + 1, 'NO')
            break
        if column_cut:
            for row in matrix:
                del row[column_minimun]
        if row_cut:
            del matrix[row_minimum]
    if not matrix:
        print 'Case #%d: %s' % (case + 1, 'YES')
