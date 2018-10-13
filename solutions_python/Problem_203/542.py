def solve():
    r,c = map(int, input().split())
    grid = []
    for i in range(r):
        row = []
        inp = input()
        for j in range(c):
            row.append(inp[j])
        grid.append(row)

    for i in range(r):
        lc  = -1
        for j in range(c):
            if ((grid[i][j] == '?') and (lc == -1)):
                continue

            if (grid[i][j] != '?'):
               k = j - 1
               while(k >= 0 and k > lc):
                   #print('k' + str(k))
                   grid[i][k] = grid[i][j]
                   k-=1
            else:
                grid[i][j] = grid[i][lc]
            lc = j

    # print("debug 2")
    # print(grid)

    lr = ""
    for i in range(r):
        if (grid[i][0] != '?'):
            lr = grid[i]
            k = i-1
            while (k >= 0 and grid[k][0] == '?'):
                grid[k] = lr
                k-=1

    k =  r-1 
    while (k >= 0 and grid[k][0] == '?'):
        grid[k] = lr
        k-=1
    
    for i in range(r):
        print(''.join(grid[i]))

    
t = int(input())
for i in range(t):
    print("Case #{0}:".format(i+1))
    solve()