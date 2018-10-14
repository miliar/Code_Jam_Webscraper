# Solution to "Pegman" for Google Code Jam 2015
# by Peter Mattsson (quantum.caffeine@gmail.com)
import sys
import heapq

dirs = {'^': (0, -1), '>': (1, 0), 'v': (0, 1), '<': (-1, 0)}
def check(grid, r, c, x, y, inc):
    while True:
        x += inc[0]
        y += inc[1]
        if not (0 <= x < c and 0 <= y < r):
            return False
        if grid[y][x] != '.':
            return True 

def solve(r, c, grid):
    result = 0
    for y in xrange(r):
        for x in xrange(c):
            if grid[y][x] == '.':
                continue
            point = grid[y][x]
            test = check(grid, r, c, x, y, dirs[point])
            if test: continue
            if any(check(grid, r, c, x, y, p) for p in dirs.values()):
                result += 1
            else:
                return "IMPOSSIBLE"
    return result
            

def cases():
    with open(sys.argv[1], 'r') as infile:
        numCases = int(infile.readline())
        for _ in range(numCases):
            r, c = (int(x) for x in infile.readline().split())
            grid = [infile.readline().rstrip() for _ in xrange(r)]
            yield r, c, grid

def main():
    with open(sys.argv[2], 'w') as outfile:
        for caseNo, case in enumerate(cases()):
            outfile.write("Case #%d: %s\n"%(caseNo + 1, str(solve(*case))))

if __name__ == "__main__":
    main()
