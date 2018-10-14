def solve(grid):
    # Stretch letters to fill rows
    for i, row in enumerate(grid):
        fill = '?'
        filled_row = row
        for j, c in enumerate(row):
            if c != '?':
                if fill == '?':
                    filled_row = c * j
                fill = c
            if fill != '?':
                filled_row += fill

        grid[i] = filled_row
        # filled_row will now be either a filled row, or all ???

    # Duplicate to fill empty rows (go forwards and backwards to fill both top and bottom
    for i in range(1, len(grid)):
        if grid[i].startswith('?'):
            grid[i] = grid[i-1]

    for i in range(len(grid)-2, -1, -1):
        if grid[i].startswith('?'):
            grid[i] = grid[i + 1]

    # Print output
    for row in grid:
        print(row)


input()
case = 0
while True:
    case += 1
    try:
        rows, cols = map(int, input().split(' '))
        grid = []
        for i in range(rows):
            grid.append(input())
    except:
        break
    print('Case #{}:'.format(case))
    solve(grid)

