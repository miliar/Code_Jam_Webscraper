def nice_print(grid):
    for line in grid:
        print("".join(line))
        

def solve(infile, outfile):
    row, col = [int(i) for i in infile.readline().split()]
    grid = []
    for i in range(row):
        line = [i for i in infile.readline().strip()]
        grid.append(line)
    #nice_print(grid)
    #print()
    
    # sweep left
    for r in range(row):
        for c in range(1, col):
            if grid[r][c-1] != '?' and grid[r][c] == '?':
                grid[r][c] = grid[r][c-1]
            
    # sweep right
    for r in range(row):
        for c in range(col - 2, -1, -1):
            if grid[r][c+1] != '?' and grid[r][c] == '?':
                grid[r][c] = grid[r][c+1]    
    
    # sweep down
    for r in range(1, row):
        for c in range(col):
            if grid[r-1][c] != '?' and grid[r][c] == '?':
                grid[r][c] = grid[r-1][c]
    
    # sweep up
    for r in range(row-2, -1, -1):
        for c in range(col):
            if grid[r+1][c] != '?' and grid[r][c] == '?':
                grid[r][c] = grid[r+1][c]
    

    #nice_print(grid)
    #print()
    
    for line in grid:
        outfile.write("".join(line) + '\n')
    #outfile.write("\n")

def main():
    infile = open('A-large.in')
    n = int(infile.readline())
    outfile = open('A-large.out', 'w')
    for i in range(1, n+1):
        #line = infile.readline().strip()
        #sol = solve(int(line))
        outfile.write("Case #{}:\n".format(i))
        sol = solve(infile, outfile)
        

main()