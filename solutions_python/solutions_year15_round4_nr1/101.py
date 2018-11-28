DIRECTIONS = {
    '^': (-1, 0),
    '>': (0, 1),
    '<': (0, -1),
    'v': (1, 0)
}

def print_map(grid):
    for row in grid:
        print ''.join(row)

def get_arrows(grid, row, col):
    if grid[row][col] == '.':
        return None
    seen = set()
    arrows = []
    while 0 <= row < len(grid) and 0 <= col < len(grid[0]):
        # print 'here', row, col, len(grid, len(grid[0]))
        if (row, col) in seen:
            return None
        if grid[row][col] != '.':
            arrows.append((row, col))
            seen.add((row, col))
            cur_arrow_v, cur_arrow_h = DIRECTIONS[grid[row][col]]
        row += cur_arrow_v
        col += cur_arrow_h
    return arrows

def solve(grid):
    R = len(grid)
    C = len(grid[0])
    chains = {}
    for row in range(R):
        for col in range(C):
            arrows = get_arrows(grid, row, col)
            # print 'found chain', row, col, arrows, chains.keys()
            if arrows is None:
                continue
            if arrows[-1] not in chains:
                chains[arrows[-1]] = arrows
            else:
                if len(arrows) > len(chains[arrows[-1]]):
                    chains[arrows[-1]] = arrows

    count = 0
    for _, chain in chains.iteritems():
        if len(chain) == 1:
            found = False
            for direction in DIRECTIONS.values():
                row, col = chain[0]
                row += direction[0]
                col += direction[1]
                while 0 <= row < len(grid) and 0 <= col < len(grid[0]):
                    if grid[row][col] != '.':
                        count += 1
                        # print 'found!', row, col
                        found = True
                        break
                    row += direction[0]
                    col += direction[1]
                if found:
                    break
            if not found:
                return 'IMPOSSIBLE'
        else:
            count += 1
    return count

input_file = open('a-large.in')
cases = int(input_file.readline().strip())
case = 0
while case < cases:
    case += 1
    R, C = [int(x) for x in input_file.readline().split()]
    grid = []
    for row in range(R):
        grid.append(list(input_file.readline().strip()))

    print "Case #{}: {}".format(case, solve(grid))
