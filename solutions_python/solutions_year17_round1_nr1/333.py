t = int(input())
toWrite = []
for test in range(1, t+1):
    dims = input()
    dimsl = dims.split()
    rows = int(dimsl[0])
    cols = int(dimsl[1])
    grid = []
    for row in range(0, rows):
        grid.append(list(input()))
    comeBack = []
    for i in range(0, rows):
        if grid[i].count("?") == len(grid[i])-1:
            for j in range(0, cols):
                if grid[i][j] == "?":
                    for h in range(0, cols):
                        if grid[i][h] != "?":
                            cur = grid[i][h]
                    grid[i][j] = cur
        elif grid[i].count("?") == len(grid[i]):
            for j in range(0, cols):
                comeBack.append(i)
        elif grid[i].count("?") == 0:
            pass
        else:
            for h in range(0, cols):
                if grid[i][h] != "?":
                    cur = grid[i][h]
                    break
            for j in range(0, cols):
                if grid[i][j] == "?":
                    grid[i][j] = cur
                else:
                    cur = grid[i][j]
    for i in comeBack:
        for j in range(0, cols):
            if i == 0:
                done = False
                pull = 1
                while not done:
                    for ri in range(1, rows):
                        if grid[ri][0] != "?":
                            done = True
                            pull = ri
                            break
                grid[i][j] = grid[pull][j]
            else:
                grid[i][j] = grid[i-1][j]
    toWrite.append("Case #" + str(test) + ":" + "\n")
    for i in range(0, rows):
        curR = ""
        for j in range(0, cols):
            curR += grid[i][j]
        if test == t and i == rows-1:
            toWrite.append(curR)
        else:
            toWrite.append(curR + "\n")
with open("output large A.out", "w") as f:
    for i in range(0, len(toWrite)):
        f.write(toWrite[i])
    
