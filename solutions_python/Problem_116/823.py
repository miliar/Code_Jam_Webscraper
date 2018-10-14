import sys

signs = {'X': 'XT', 'O': 'OT'}

def check(data, sign):
    for i in data:
        if i not in signs[sign]:
            return 0
    return 1

def solve(grid):
    # check rows
    for row in grid:
        if check(row, 'X'): return 'X won'
        if check(row, 'O'): return 'O won'

    # check columns
    for i in range(4):
        column = []
        for j in range(4):
            column.append(grid[j][i])
        if check(column, 'X'): return 'X won'
        if check(column, 'O'): return 'O won'

    # check diagonal
    diag1 = []
    diag2 = []
    for i in range(4):
        for j in range(4):
            if i == j: diag1.append(grid[i][j])
            if i + j == 3: diag2.append(grid[i][j])
    if check(diag1, 'X'): return 'X won'
    if check(diag2, 'X'): return 'X won'
    if check(diag1, 'O'): return 'O won'
    if check(diag2, 'O'): return 'O won'

    for row in grid:
        for i in row:
            if i == '.':
                return 'Game has not completed'
    return 'Draw'

def main():
    try:
        path = sys.argv[1]
        results = []
        with open(path, 'r') as f:
            cases = int(f.readline())

            for i in range(cases):
                line = ''
                grid = []
                row = []
                while True:
                    line = f.readline().strip()
                    if len(line) == 0:
                        break
                    row = [x for x in line]
                    grid.append(row)
                results.append("Case #{0}: {1}{2}".format(i + 1, solve(grid), '\n' if i < cases - 1 else ''))
        with open(path + '-results', 'w') as fr:
            fr.write("".join(results))
    except FileNotFoundError:
        print("Couldn't find file!")
    except IndexError:
        print("usage: tic_tac_toe_tomek.py <path_to_file>")

main()
