directions = "<>^v"
def blocked(grid, i, j, direction):
    diff = {"<":-1, ">":1, "^":-1, "v":1}
    if direction in "<>":
        k = j
        k += diff[direction]
        while k >= 0 and k < len(grid[i]):
            if grid[i][k] != '.':
                return True
            k += diff[direction]
        return False
    else:
        k = i
        k += diff[direction]
        while k >= 0 and k < len(grid):
            if grid[k][j] != '.':
                return True
            k += diff[direction]
        return False

def changes(grid):
    tochange = 0
    for i, row in enumerate(grid):
        for j, cell in enumerate(row):
            if cell != '.':
                safe = {d:blocked(grid,i,j,d) for d in directions}
                if not any(safe.values()):
                    return "IMPOSSIBLE"
                elif not safe[cell]:
                    tochange +=1
    return tochange

for case in range(input()):
    print "Case #%s:" % (case+1),
    R, C = map(int, raw_input().split())
    grid = []
    for i in xrange(R):
        grid.append(raw_input().strip())
    print changes(grid)
