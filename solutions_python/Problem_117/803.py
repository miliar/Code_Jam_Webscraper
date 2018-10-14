from sys import stdin, stdout
lines = stdin.read().split('\n')
ntests = int(lines.pop(0))

for test in range(ntests):
    stdout.write("Case #"+str(test+1)+": ")
    n,m = map(int,lines.pop(0).split(' '))
    grid = []
    hs = set()
    for i in range(n): 
        grid.append(map(int,lines.pop(0).split(' '))) 
        hs.update(grid[i])
    hs = sorted(list(hs))
    possible = True
    for hsi in range(0,len(hs)-1):
        #print grid
        h = hs[hsi]
        nh = hs[hsi+1]
        rowmaxes = []
        colmaxes = []
        for y in range(n): rowmaxes.append(max(grid[y]))
        for x in range(m): colmaxes.append(max([grid[i][x] for i in range(n)]))
        #print rowmaxes, colmaxes
        for y in range(n):
            for x in range(m):
                if grid[y][x] == h:
                    if grid[y][x]<rowmaxes[y] and grid[y][x]<colmaxes[x]: possible = False
                    grid[y][x] = nh
        if not possible: break
    if possible: stdout.write("YES\n")
    else: stdout.write("NO\n")