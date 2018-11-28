import sys


def merge(a, b):
    for k in a.keys():
        a[k] += b[k]


def msg(pos, s):
    print('Case #{0}: {1}'.format(pos, s))


def solve_table(pos, table, rows, cols):
    #first = table[0][0]

    #print('rows {0} cols {1}'.format(rows, cols))
    minColInRow = [1000] * rows
    maxColInRow = [0] * rows
    minRowInCol = [1000] * cols
    maxRowInCol = [0] * cols

    # calc mins and maxes
    for row in range(rows):
        for col in range(cols):
            x = table[row][col]
            minColInRow[row] = min(minColInRow[row], x)
            maxColInRow[row] = max(maxColInRow[row], x)
            minRowInCol[col] = min(minRowInCol[col], x)
            maxRowInCol[col] = max(maxRowInCol[col], x)

    #print(minColInRow)
    #print(maxColInRow)
    #print(minRowInCol)
    #print(maxRowInCol)

    def win(row, col):
        x = table[row][col]
        s = 'table[{0}][{1}] = {2} ({3}, {4})'.format(row, col, x,
                                                      maxColInRow[row],
                                                      maxRowInCol[col])
        #print(s)
        #print(x, maxColInRow[row], maxRowInCol[col])
        return ((maxColInRow[row] <= x) or (maxRowInCol[col] <= x))

    for row in range(rows):
        for col in range(cols):
            if not win(row, col):
                return msg(pos, 'NO')

    return msg(pos, 'YES')


def solve(filename):
    with open(filename) as f:
        N = int(f.readline().strip())

        for i in range(N):
            rows, cols = map(int, f.readline().strip().split(' '))
            table = []
            for j in range(rows):
                line = f.readline().strip().split(' ')
                table.append(map(int, line))
                #print(line)
            #print('table {0}'.format(table))
            solve_table(i + 1, table, rows, cols)
            #print('')


if __name__ == '__main__':
    solve(sys.argv[1])
