T = int(input())

for t in range(1, T+1):
    ans  = 1

    R, C = map(int, input().split())

    grid = []
    for r in range(R):
        grid.append(list(input()))

    # for each line:
    #  find first letter, fill left
    #  fill letter to right until next letter

    # find first on ? line, fill upwards
    # then fill down til next non ? line

    qlines = set()
    firstnonq = None

    for i, row in enumerate(grid):
        fill = None
        for col in row:
            if col != '?':
                fill = col
                if firstnonq is None:
                    firstnonq = i
                break
        else:
            qlines.add(i)
            continue

        for j, col in enumerate(row):
            if col == '?':
                row[j] = fill
            else:
                fill = col

    fillrow = grid[firstnonq]
    for i, row in enumerate(grid):
        if i in qlines:
            grid[i] = fillrow
        else:
            fillrow = row


    print('Case #{}:'.format(t))
    for row in grid:
        print(''.join(row))