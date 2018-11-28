""" Fill cake with grid initials"""

from sys import stdin

def find_first_non_quest(row, cols):
    for i in range(cols):
        if row[i] != '?':
            return i
    return -1

def solve_cakes(rows, cols, grid):
    # First fill row wise.
    new_grid = []
    for row in grid:
        # find first character not a ?. If none, leave row.
        first_non_quest = find_first_non_quest(row,cols)
        if first_non_quest == -1:
            new_grid.append(row)
            continue

        current_char = row[first_non_quest]
        new_row = ""

        # Fill in rows with next adjacent char.
        for i in range(cols):
            if row[i] != '?':
                current_char = row[i]
            new_row = new_row + current_char

        new_grid.append(new_row)

    #now do the same thing column wise
    grid = []
    for i in range(rows):
        grid.append("")

    for i in range(cols):
        column = ""
        for j in range(rows):
            column = column + new_grid[j][i]
        first_non_quest = find_first_non_quest(column, rows)
        #There should always be one

        current_char = new_grid[first_non_quest][i]

        for j in range(rows):
            if new_grid[j][i] != '?':
                current_char = new_grid[j][i]
            grid[j] = grid[j] + current_char
    return grid

def main():
    test_cases  = int(stdin.readline())
    for i in range(1, test_cases + 1):
        rows, cols = (int(z) for z in stdin.readline().split())
        grid = []
        for x in range(rows):
            grid.append(stdin.readline().strip())
        result = solve_cakes(rows, cols, grid)

        print("Case #%s:" % str(i))
        for row in result:
            print(row)

main()
