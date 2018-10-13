from collections import defaultdict
import sys
import copy
import pprint
def testCase(grid):
    emptyRow = -1
    for c in range(len(grid[0])):
        last = "?"
        for r in range(len(grid)):
            #print r,c, grid[r][c], last
            if grid[r][c] == last:
                continue
            else:
                if grid[r][c] == "?":

                    grid[r][c] = copy.copy(last)
                    #print ' k',r,c, last
                else:
                    if last == "?":
                        for j in range(0, r+1):
                            #print ' j',j, c, grid[r][c]
                            grid[j][c] = copy.copy(grid[r][c])
                    last = grid[r][c]
        if last == "?":
            #print c, emptyRow
            if  c > emptyRow+ 1:
                for r in range(len(grid)):
                    grid[r][c] = grid[r][c-1]
            else:
                emptyRow += 1
    for c in range(emptyRow+1):
        for r in range(len(grid)):
            grid[r][c] = grid[r][emptyRow+1]


    return grid





testcount = int(sys.stdin.readline())
for i in range(testcount):
    r,c = map(int, sys.stdin.readline().strip("\n").split(" "))
    grid = []
    for j in range(r):
        grid.append(list(sys.stdin.readline().strip("\n")))

    answer = testCase(grid)

    print("Case #{}:".format(i+1))
    for row in answer:
        print "".join(row)
