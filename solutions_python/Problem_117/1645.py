import sys
def same(row):
    val = row[0]
    for stuff in row[1:]:
        if stuff != val:
            return False
    return True

def lowest_in_column(val, grid, col):
    for row in grid:
        if row[col] > val:
            return True
    return False

def valid(grid):
    for row in grid:
        #Everything on this row is the same
        if same(row):
            continue
        else:
            lowest = min(row)
            for col,val in enumerate(row):
                if val == lowest:
                    if lowest_in_column(val, grid, col):
                        return "NO"
    return "YES"

if __name__ == '__main__':
    lines = [line.strip() for line in sys.stdin]
    cases = int(lines[0])

    start = 1
    for i in range(cases):
        n, m = [int(val) for val in lines[start].split()]
        grid = []
        for j in range(n):
            grid.append([int(val) for val in lines[start + j + 1].split()])

        start += n + 1
        print "Case #%d: %s" % (i + 1, valid(grid))
