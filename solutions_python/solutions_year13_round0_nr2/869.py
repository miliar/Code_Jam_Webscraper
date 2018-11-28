__author__ = 'Mad Cow'


def Lawnmower(path):
    with open(path, 'r') as f:
        case = 1
        output = ''
        n_cases = int(f.readline().strip())
        for i in range(n_cases):
            nm = f.readline().strip().split(' ')
            n = int(nm[0])
            m = int(nm[1])
            grid = []
            for j in range(n):
                grid.append([int(k) for k in f.readline().strip().split(' ')])
            output += "Case #" + str(case) + ": " + Judge(grid, n, m)
            if case < n_cases:
                output += '\n'
            case += 1
    with open ('Lawnmower.out', 'w') as f:
        f.write(output)


def Judge(grid, n, m):
    minRow = [max(grid[i]) for i in range(n)]
    minColumn = [max([grid[j][i] for j in range(n)]) for i in range(m)]
    for i in range(n):
        for j in range(m):
            if not grid[i][j] == min(minRow[i], minColumn[j]):
                return 'NO'
    return 'YES'

Lawnmower('B-large.in')


