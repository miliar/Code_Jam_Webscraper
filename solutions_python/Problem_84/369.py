
import sys
import re

cases = int(sys.stdin.readline())
case = 0
def main():
    (r,c) = [int(x) for x in sys.stdin.readline().strip().split(None)]
    grid = [ sys.stdin.readline() for x in range(0,r) ]
    bad = False
    for i in range(0,r):
        try:
            for j in range(0,c):
                if grid[i][j] == "#":
                    if grid[i][j+1] != "#" or grid[i+1][j] != "#" or grid[i+1][j+1] != "#":
                        bad = True
                    grid[i] = grid[i][:j] + "/\\" + grid[i][j+2:]
                    grid[i+1] = grid[i+1][:j] + "\\/" + grid[i+1][j+2:]
            if "#" in grid[i]:
                bad = True
        except:
            bad = True
    if bad:
        print "Impossible"
    else:
        for x in grid:
            print x.strip()


for i in range(1,cases+1):
    print "Case #%d:" % (i)
    main()
