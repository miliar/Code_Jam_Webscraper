

def solve(grid,R,C):
    for i in range(R):
        for j in range(C):
            if grid[i][j] != "?":
                initial = grid[i][j]
                for k in range(j-1,-1,-1):
                    if grid[i][k] != "?":
                        break
                    else:
                        grid[i][k] = initial

                for k in range(j+1,C):
                    if grid[i][k] != "?":
                        break
                    else:
                        grid[i][k] = initial

    for i in range(R):
        for j in range(C):
            flag = 0
            if grid[i][j] == "?":
                for k in range(i-1,-1,-1):
                    if grid[k][j] != "?":
                        flag = 1
                        grid[i][j]=grid[k][j]
                        break
                if not flag:
                    for k in range(i+1,R):
                        if grid[k][j] != "?":
                            grid[i][j]=grid[k][j]
                            break

    return grid

f = open("A-large.in","r")
g = open("output.txt","w")

T = int(f.readline())

for i in range(T):
    [R,C] = [int(j) for j in f.readline().split()]
    grid = [[k for k in f.readline().strip()] for j in range(R)]

    ans = solve(grid,R,C)

    g.write("Case #{}:\n".format(i+1))
    for row in ans:
        g.write("".join(row)+"\n")


f.close()
g.close()
