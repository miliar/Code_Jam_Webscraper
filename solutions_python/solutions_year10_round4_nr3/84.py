import sys, itertools
from pprint import pprint
from collections import namedtuple

output_line = "Case #{N:d}: {T:d}"

#minimize cost, 
if __name__ == "__main__":
    infile, outfile = sys.argv[1:]
    with open(infile, "r") as inhandle, open(outfile, "w") as outhandle:
        C = int(inhandle.readline())
        for c in range(C):
            grid = [[0] * 100 for i in range(100)]

            R = int(inhandle.readline())
            for r in range(R):
                x1, y1, x2, y2 = map(int, inhandle.readline().split())
                for y in range(y1 - 1, y2):
                    for x in range(x1 - 1, x2):
                        grid[y][x] = 1

            #pprint(grid)
            for seconds in range(2000):
                if all(all(not grid[y][x] for x in range(len(grid[y]))) for y in range(len(grid))):
                    break
                newgrid = [[0] * 100 for i in range(100)]
                for y in range(1, 100):
                    for x in range(1, 100):
                        if (grid[y - 1][x] and grid[y][x - 1]) or (grid[y][x] and (grid[y - 1][x] or grid[y][x - 1])):
                            newgrid[y][x] = 1
                grid = newgrid

            print(output_line.format(N=c + 1, T=seconds), file=outhandle)
