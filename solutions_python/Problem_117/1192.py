num_test_cases = int(input())

def main(test_case):
    size_line = input()
    rows, columns = [int(i) for i in size_line.split()]

    grid = []

    for row in range(rows):
        line = input()
        grid.extend([[int(i) for i in line.split()]])

    row_maxes = {row: max(grid[row]) for row in range(rows)}

    column_maxes = {column: max(row[column] for row in grid) for column in range(columns)}

    for i, row in enumerate(grid):
        for j, column in enumerate(row):
            if column not in (row_maxes[i], column_maxes[j]):
                print("Case #{}: NO".format(test_case + 1))
                return
    else:
        print("Case #{}: YES".format(test_case + 1))

    return

for test_case in range(num_test_cases):
    main(test_case)
