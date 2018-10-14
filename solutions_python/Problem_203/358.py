def column(array, i):
    return [row[i] for row in array]

def find_first_letter(row):
    for item in row:
        if item != "?":
            return item
    return "?"

def assign_cake(r, c, grid):

    for row in range(r):
        letter = find_first_letter(grid[row])
        for col in range(c):
            if grid[row][col] == "?":
                grid[row][col] = letter
            else:
                letter = grid[row][col]

    for col in range(c):
        letter = find_first_letter(column(grid, col))
        for row in range(r):
            if grid[row][col] == "?":
                grid[row][col] = letter
            else:
                letter = grid[row][col]

    return grid


def print_cases(func):
    for i in range(1, int(input())+1):
        r, c = map(int,input().split())
        array = [row for row in [list(input()) for _ in range(r)]]
        output = "\n".join(["".join([item for item in row]) for row in func(r, c, array)])
        print("Case #{}:\n{}".format(i, output))

if __name__ == "__main__":
    print_cases(assign_cake)

