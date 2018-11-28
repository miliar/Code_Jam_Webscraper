T = input()
for t in range(T):
    R, C = map(int, raw_input().split())
    grid = []
    for r in range(R):
        grid.append(list(raw_input().strip()))
    last_row = ['?'] * C
    for r in range(R):
        is_empty = True
        for c in range(C):
            if grid[r][c] != '?':
                is_empty = False
                break

        if is_empty:
            for c in range(C):
                grid[r][c] = last_row[c]
            continue

        last_letter = '?'
        for c in range(C):
            if grid[r][c] == '?':
                grid[r][c] = last_letter
            else:
                last_letter = grid[r][c]
        last_letter = '?'
        for c in range(C)[::-1]:
            if grid[r][c] == '?':
                grid[r][c] = last_letter
            else:
                last_letter = grid[r][c]
        last_row = list(grid[r])

    last_row = ['?'] * C
    for r in range(R)[::-1]:
        is_empty = True
        for c in range(C):
            if grid[r][c] != '?':
                is_empty = False
                break
        if is_empty:
            for c in range(C):
                grid[r][c] = last_row[c]
        else:
            last_row = list(grid[r])

    print("Case #" + str(t+1) + ":")
    for row in grid:
        print(''.join(row))

