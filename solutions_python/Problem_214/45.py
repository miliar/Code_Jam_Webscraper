import itertools

def move(cell, grid, direction):
    x, y = cell
    dx, dy = direction

    x += dx
    y += dy

    if not (0 <= x < len(grid[0]) and 0 <= y < len(grid)):
        return "end"

    if grid[y][x] == "#":
        return "end"

    if grid[y][x] in "|-":
        return "crash"

    if grid[y][x] == "/":
        dx, dy = -dy, dx

    elif grid[y][x] == "\\":
        dx, dy = dy, -dx

    return (x, y), (dx, dy)


def get_horizontal_cells(x, y, grid):
    # Left
    cell = (x, y)
    direction = (-1, 0)
    horizontal_cells = set()

    while True:
        new_move = move(cell, grid, direction)

        if new_move == "crash":
            return None
        elif new_move == "end":
            break

        cell, direction = new_move
        a, b = cell
        if grid[b][a] == ".":
            horizontal_cells.add(cell)

    # Right
    cell = (x, y)
    direction = (1, 0)

    while True:
        new_move = move(cell, grid, direction)

        if new_move == "crash":
            return None
        elif new_move == "end":
            break

        cell, direction = new_move
        a, b = cell
        if grid[b][a] == ".":
            horizontal_cells.add(cell)

    return horizontal_cells


def get_vertical_cells(x, y, grid):
    # Up
    cell = (x, y)
    direction = (0, -1)
    vertical_cells = set()

    while True:
        new_move = move(cell, grid, direction)

        if new_move == "crash":
            return None
        elif new_move == "end":
            break

        cell, direction = new_move
        a, b = cell
        if grid[b][a] == ".":
            vertical_cells.add(cell)

    # Down
    cell = (x, y)
    direction = (0, 1)

    while True:
        new_move = move(cell, grid, direction)

        if new_move == "crash":
            return None
        elif new_move == "end":
            break

        cell, direction = new_move
        a, b = cell
        if grid[b][a] == ".":
            vertical_cells.add(cell)

    return vertical_cells


with open("C-small-attempt2.in") as infile:
    with open("C-small-attempt2.out", "w") as outfile:
        cases = int(next(infile))

        for case in range(1, cases+1):
            r, c = map(int, next(infile).split())
            grid = []

            for _ in range(r):
                grid.append(list(next(infile).rstrip()))

            covered_cells = []
            to_cover_cells = set()
            impossible = False
            lookup = {}

            for y in range(r):
                for x in range(c):
                    if grid[y][x] == ".":
                        to_cover_cells.add((x, y))

            for y in range(r):
                for x in range(c):
                    if grid[y][x] in "|-":
                        horizontal_cells = get_horizontal_cells(x, y, grid)
                        vertical_cells = get_vertical_cells(x, y, grid)

                        if horizontal_cells is vertical_cells is None:
                            impossible = True
                        elif horizontal_cells is None:
                            lookup[x, y] = 2
                            to_cover_cells -= vertical_cells
                        elif vertical_cells is None:
                            lookup[x, y] = 1
                            to_cover_cells -= horizontal_cells
                        elif horizontal_cells == vertical_cells:
                            lookup[x, y] = 1
                            to_cover_cells -= horizontal_cells
                        else:
                            covered_cells.append(((x, y), horizontal_cells, vertical_cells))


            # print(covered_cells)
            print(case, len(covered_cells))

            solution = None
            if not impossible:
                for x in itertools.product([1, 2], repeat=len(covered_cells)):
                    a = [z[i] for i, z in zip(x, covered_cells)]
                    if any(q is None for q in a):
                        continue

                    f = set()
                    for q in a:
                        f.update(q)

                    if f >= to_cover_cells:
                        solution = x
                        break

                if solution is None:
                    impossible = True

            if impossible:
                print("Case #{}: IMPOSSIBLE".format(case), file=outfile)
            else:
                print("Case #{}: POSSIBLE".format(case), file=outfile)
    
                for a, s in zip(covered_cells, solution):
                    lookup[a[0]] = s

                for y in range(r):
                    for x in range(c):
                        if (x, y) in lookup:
                            grid[y][x] = " -|"[lookup[x, y]]

                for row in grid:
                    print("".join(row), file=outfile)
                            
                
                        
                            
