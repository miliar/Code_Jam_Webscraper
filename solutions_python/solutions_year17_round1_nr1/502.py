import re
        
T = int(input().strip())
for test in range(T):
    n, m = map(int, input().strip().split())
    grid = []
    
    for i in range(n):
        grid.append(list(input().strip()))
    
    for i in range(n):
        for j in range(m):
            if grid[i][j] != "?":
                for k in range(j - 1, -1, -1):
                    if grid[i][k] == "?":
                        grid[i][k] = grid[i][j]
                    else:
                        break
                
        for j in range(m - 1, -1, -1):
            if grid[i][j] != "?":
                break
        for k in range(j + 1, m):
            grid[i][k] = grid[i][j]
    

    for i in range(n):
        if len(re.findall(r"\?{%d}" % m, "".join(grid[i]))) == 0:
            for j in range(i - 1, -1, -1):
                if len(re.findall(r"\?{%d}" % m, "".join(grid[j]))) != 0:
                    grid[j] = grid[i]
                else:
                    break
            
    for i in range(n - 1, -1, -1):
        if len(re.findall(r"\?{%d}" % m, "".join(grid[i]))) == 0:
            break
    for j in range(i + 1, n):
        grid[j] = grid[i]
    print("Case #%d:" % (test + 1))
    for i in range(n):
        print("".join(grid[i]))