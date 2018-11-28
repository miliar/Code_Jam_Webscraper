t = input()
for i in range(1, t+1):
    h, w = map(int, raw_input().split())
    grid = [map(int, raw_input().split()) for x in range(h)]
    trail = [[[] for y in range(w)] for x in range(h)]
    sinks = []
    for x in range(h):
        for y in range(w):
            best = x, y
            for dx, dy in ((-1,0), (0, -1), (0,1), (1,0)):
                if 0 <= x+dx < h and 0 <= y+dy < w and grid[x+dx][y+dy] < grid[best[0]][best[1]]:
                    best = x+dx, y+dy
            if best != (x, y):
                trail[best[0]][best[1]].append((x,y))
            else:
                sinks.append((x,y))
    label = 1
    for x, y in sinks:
        todo = trail[x][y]
        while todo:
            a, b = todo.pop()
            todo += trail[a][b]
            grid[a][b] = label
        grid[x][y] = label
        label += 1
    labs = {}
    label = 'a'
    for x in range(h):
        for y in range(w):
            if grid[x][y] not in labs:
                labs[grid[x][y]] = label
                grid[x][y] = label
                label = chr(ord(label)+1)
            else:
                grid[x][y] = labs[grid[x][y]]
    print "Case #"+str(i)+":"
    print '\n'.join([' '.join(x) for x in grid])
