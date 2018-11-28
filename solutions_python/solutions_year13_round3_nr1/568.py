def nCons(n, s):
    total=0
    while len(s)>0:
        tmp = s.pop()
        if tmp not in vowels:
            total+=1
            if total >= n:
                return True
        else:
            break
    if len(s) == 0:
        return False
    return nCons(n, s)

vowels=['a', 'e', 'i', 'o', 'u']

inp=raw_input
t=int(inp())
for c in range(t):
    name, n = inp().split()
    n = int(n)
    grid=[]
    for i in range(len(name)):
        grid.append([])
        for j in range(i+1):
            grid[-1].append(False)
    for x in range(len(name)):
        for y in range(len(name) - x):
            i = y
            j = x + y
            if i<j and j>0 and (grid[j][i+1] or grid[j-1][i]):
                grid[j][i] = True
            else:
                if nCons(n, list(name[i:j+1])):
                    grid[j][i] = True
    count = reduce(lambda x, y: x + len(filter(lambda z: z, y)), grid, 0)
    print "Case #%d: %d" % (c+1, count)
