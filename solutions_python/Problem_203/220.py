def first_non_q(row):
    for index, square in enumerate(row):
        if square != "?":
            return index, square

def row_has_character(row):
    for square in row:
        if square != "?":
            return True
    return False

t = int(input())
for i in range(1, t + 1):
    r, c = [int(s) for s in input().split(" ")]
    grid = []
    for j in range(0, r):
        grid.append(list(input()))
    
    for row in grid:
        if row_has_character(row):
            startCharPos, startChar = first_non_q(row)
            for j in range(0, startCharPos):
                row[j] = startChar
            prevChar = startChar
            for j in range(startCharPos + 1, len(row)):
                if row[j] == '?':
                    row[j] = prevChar
                else:
                    prevChar = row[j]
    for j in range(len(grid) - 1):
        if row_has_character(grid[j]) and not row_has_character(grid[j + 1]):
            grid[j + 1] = grid[j]
    for j in reversed(range(1, len(grid))):
        if row_has_character(grid[j]) and not row_has_character(grid[j - 1]):
            grid[j - 1] = grid[j]
    print("Case #{}:".format(i))
    for row in grid:
        print(''.join(row))
    #print("Case #{}: {} {}".format(i, n + m, n * m))