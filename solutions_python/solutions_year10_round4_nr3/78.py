#!/opt/local/bin/python3.1
import sys

def get_grid(size):
    '''size*size rectangle filled with 0'''
    res = []
    for i in range(size):
        res.append([])
        for j in range(size):
            res[i].append(0)
    return res

def place_bacteria(grid, x1, y1, x2, y2):
    '''caution:

    x1, y1, x2, y2: 1-origin
    grid: 0-origin
    '''
    for x in range(x1 - 1, x2):
        for y in range(y1 - 1, y2):
            grid[x][y] = 1

def advance(grid, size):
    for x in range(size - 1, -1, -1):
        for y in range(size - 1, -1, -1):
            if not x:
                west = 0
            else:
                west = grid[x - 1][y]

            if not y:
                north = 0
            else:
                north = grid[x][y - 1]

            if not west and not north:
                grid[x][y] = 0
            elif west and north:
                grid[x][y] = 1
            else:
                pass

def check_death(grid, size):
    for x in range(size):
        for y in range(size):
            if grid[x][y]:
                return False
    return True

def count_seconds(grid, size):
    seconds = 0
    while not check_death(grid, size):
        advance(grid, size)
        seconds += 1
    return seconds

def main(argv=None):
    if not argv:
        argv = sys.argv

    infile = open(argv[1], 'r')
    outfile = open(argv[2], 'w')
    size = int(argv[3])

    n_testcases = int(infile.readline())
    count = 0

    for line in infile:
        count += 1
        n_rect = int(line)

        grid = get_grid(size)
        for i in range(n_rect):
            x1, y1, x2, y2 = [int(n) for n in infile.readline()[:-1].split()]
            place_bacteria(grid, x1, y1, x2, y2)

        print('Case #{0}: {1}'.format(count, count_seconds(grid, size)), file=outfile)

    if not n_testcases == count:
        print('{0} lines left. something wrong with the input file'.format(n_testcases - count))

if __name__ == '__main__':
    sys.exit(main())
