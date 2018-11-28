t = int(raw_input())
for num in xrange(1, t + 1):
    r,c = [int(s) for s in raw_input().split(" ")] 

    grid = []
    for row in xrange(r):
        grid.append(list(raw_input()))


    rowChain= -1
    for row in range(len(grid)):
        rowBearer = "?"
        for col in range(c):
            if not grid[row][col]=="?":
                if rowBearer == "?":
                    rowBearer = grid[row][col]
                    for i in range(col):
                        grid[row][i]=rowBearer
                rowBearer = grid[row][col]
            else:
                grid[row][col]=rowBearer
        if rowBearer =="?":
            if rowChain == row-1:
                rowChain+=1
            else :
                for i in range(c):
                    grid[row][i]=grid[row-1][i]
        elif rowChain == row-1:
            for rr in reversed(range(rowChain+1)):
                for cc in range(c):
                    grid[rr][cc]=grid[rr+1][cc]

                


    #val = [int(s) for s in raw_input().split(" ")]  # read a list of integers, 2 in this case
    ret  = grid 
    print "Case #" +str(num) + ": " 
    for j in range(r):
        print ''.join(grid[j])
