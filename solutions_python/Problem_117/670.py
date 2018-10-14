def game():
    f = open("B-small-attempt0.in", "r")
    output = open("B-small-attempt0.out", "w")
    first = f.readline()
    T = int(first)
    case = 1

    while case < T+1:
        size = f.readline()
        size = size.split(" ")
        N = int(size[0])
        M = int(size[1])
        #print N,M
        grid = [[]]*N
        for i in range(N):
            grid[i] = f.readline()[:-1].split(" ")
        #print grid
        res = "Case #" + str(case) + ": " + result(grid, N, M)+ "\n"
        #print res
        output.write(res)
        case = case+1

def result(grid, N, M):
    for i in range(N):
        for j in range(M):
            if (grid[i][j] == "1"):
                if(canExit(grid, N, M, "1", i, j) == 0):
                    #print "###", i, j
                    return "NO"
    return "YES"

def canExit(grid, N, M, string, i, j):
    bool_hor = True
    #Check horizontal
    if(grid[i].count(string) == M):
        #print "hori"
        return 1
    
    #Check vertical
    for vert in range(N):
        if(grid[vert][j]!=string):
            #print "verti", grid[i][vert], i, vert
            return 0
    
    return 1

game()
