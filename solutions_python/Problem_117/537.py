
def readFile(filename):
    f = open(filename, 'r')
    totalCases = int(f.readline()[:-1])
    grids = []
    for _ in range(totalCases):
        rows, _ = f.readline()[:-1].split()
        grid = []
        for r in range(int(rows)):
            line = f.readline()[:-1]
            grid.append(line.split())
        grids.append(grid)
    f.close()
    return grids

def checkPattern(grid):
    rows = [map(int, row) for row in grid]
    columns = []
    width = len(grid[0]) if len(grid) > 0 else 0
    height = len(grid)
    for c in range(width):
        column = []
        for r in range(height):
            column.append(int(grid[r][c]))
        columns.append(column)
    #lines = (rows, columns)
    for row in rows:
        for cI, element in enumerate(row):
            column = columns[cI]
            if max(row) > element and max(column) > element:
                return "NO"
    return "YES"

def checkGameState(infile, outfile):
    grids = readFile(infile)
    output = []
    for index, grid in enumerate(grids):
        result = "Case #" + str(index + 1) + ": " + checkPattern(grid)
        #print "grid:\n" + "\n".join(' '.join([x if len(x)>0 else '_' for x in row]) for row in grid) + "\nresult:" + result
        output.append(result)
    output = '\n'.join(output)
    f = open(outfile, 'w')
    f.write(output)

input = 'B-large.in'
output = 'B-large-output.txt'
checkGameState(input, output)