def next_char(row_index, col_index, grid):
    row = grid[row_index]
    for c in row[col_index:]:
        if c != '?':
            return c

    return None


def next_char_r(row_index, col_index, grid):
    for r in range(row_index, len(grid)):
        row = grid[r]
        if row[col_index] != '?':
            return row[col_index]

    return None


def solve(r, c, grid):
    empty_rows = []
    for i in range(r):
        next_c = next_char(i, 0, grid)
        if next_c is None:
            empty_rows.append(i)
            continue

        last_c = next_c

        for j in range(c):
            if grid[i][j] == '?':
                grid[i][j] = last_c
            else:
                last_c = grid[i][j]

    for j in range(c):
        next_r = next_char_r(0, j, grid)
        if next_r is None:
            raise Exception()

        last_r = next_r

        for i in range(r):
            if grid[i][j] == '?':
                grid[i][j] = last_r
            else:
                last_r = grid[i][j]

    return grid


def main():
    num_cases = int(raw_input())

    for case_index in range(num_cases):
        case_line = raw_input()
        r, c = [long(x) for x in case_line.split(' ')]

        grid = []
        for i in range(r):
            grid.append(list(raw_input()))

        answer = solve(r, c, grid)

        print("Case #{}:".format(case_index+1))
        for row in answer:
            print("".join(row))

main()
