import sys, collections

inputfile = file(sys.argv[1])
outputfile = file(sys.argv[2], 'w')

def findgridneeds(grid):
    #print grid
    needs = {}# collections.defaultdict(list)
    needscovering = set()
    R, C = len(grid), len(grid[0])
    #print R, C
    #print grid
    for i in xrange(R):
        for j in xrange(C):
            if grid[i][j] == '|' or grid[i][j] == '-':
                needs[(i,j)] = []
            if grid[i][j] == '.':
                needscovering.add((i,j))
    for i in xrange(R):
        lastemmitter = None
        dangerous = False
        for j in xrange(C):
            if grid[i][j] == '-' or grid[i][j] == '|':
                if lastemmitter != None:
                    dangerous = True
                else:
                    lastemmitter = (i, j)
            elif grid[i][j] == '#':
                if not dangerous and lastemmitter != None:
                    needs[lastemmitter].append('-')
                lastemmitter = None
                dangerous = False
        if not dangerous and lastemmitter != None:
            needs[lastemmitter].append('-')
    for j in xrange(C):
        lastemmitter = None
        dangerous = False
        for i in xrange(R):
            if grid[i][j] == '-' or grid[i][j] == '|':
                if lastemmitter != None:
                    dangerous = True
                else:
                    lastemmitter = (i, j)
            elif grid[i][j] == '#':
                if not dangerous and lastemmitter != None:
                    needs[lastemmitter].append('|')
                lastemmitter = None
                dangerous = False
        if not dangerous and lastemmitter != None:
            needs[lastemmitter].append('|')
    #print needs
    while True:
        #print needs
        coveredby = [[[] for _ in xrange(C)] for _ in xrange(R)]
        for (i, j) in needs:
            for c in needs[(i,j)]:
                if c == '|':
                    dif = 1
                    while i + dif < len(grid):
                        if grid[i+dif][j] == '#':
                            break
                        coveredby[i+dif][j].append((i,j))
                        dif += 1
                    dif = -1
                    while i + dif >= 0:
                        if grid[i+dif][j] == '#':
                            break
                        coveredby[i+dif][j].append((i,j))
                        dif -= 1
                else:
                    dif = 1
                    while j + dif < len(grid[i]):
                        if grid[i][j+dif] == '#':
                            break
                        coveredby[i][j+dif].append((i,j))
                        dif += 1
                    dif = -1
                    while j + dif >= 0:
                        if grid[i][j+dif] == '#':
                            break
                        coveredby[i][j+dif].append((i,j))
                        dif -= 1
        change = False
        #print coveredby
        for i in xrange(R):
            for j in xrange(C):
                if len(coveredby[i][j]) == 0 and grid[i][j] == '.':
                    print 'prob', i,j
                    for k in needs:
                        needs[k] = []
                    return needs, needscovering
                if len(coveredby[i][j]) == 1:
                    ei, ej = coveredby[i][j][0]
                    if len(needs[(ei, ej)]) != 2:
                        continue
                    change = True
                    if ei == i:
                        needs[(ei, ej)].remove('|')
                    else:
                        needs[(ei, ej)].remove('-')
        if not change:
            break
    return needs, needscovering

def checkconfiguration(grid, emitters, needscovering):
    #print grid, needscovering
    for (i,j) in emitters:
        if grid[i][j] == '|':
            dif = 1
            while i + dif < len(grid):
                if grid[i+dif][j] == '#':
                    break
                needscovering.discard((i+dif, j))
                dif += 1
            dif = -1
            while i + dif >= 0:
                if grid[i+dif][j] == '#':
                    break
                needscovering.discard((i+dif, j))
                dif -= 1
        else:
            dif = 1
            while j + dif < len(grid[i]):
                if grid[i][j+dif] == '#':
                    break
                needscovering.discard((i, j+dif))
                dif += 1
            dif = -1
            while j + dif >= 0:
                if grid[i][j+dif] == '#':
                    break
                needscovering.discard((i, j+dif))
                dif -= 1
    #print needscovering
    return len(needscovering) == 0

def permsemmitters(i, emmitters, needs, needscovering, grid):
    if i == len(emmitters):
        return checkconfiguration(grid, emmitters, set(needscovering))
    for c in needs[emmitters[i]]:
        grid[emmitters[i][0]][emmitters[i][1]] = c
        if permsemmitters(i+1, emmitters, needs, needscovering, grid):
            return True
    return False


for case in xrange(int(inputfile.readline())):
    R, C = map(int, inputfile.readline().split())
    grid = []
    for _ in xrange(R):
        grid.append(list(inputfile.readline().strip()))
    print case
    #print grid
    needs, needscovering = findgridneeds(grid)
    impossible = False
    for l in needs.values():
        if len(l) == 0:
            impossible = True
            break
    if not impossible:
        impossible = not permsemmitters(0, list(needs.keys()), needs, needscovering, grid)
    if impossible:
        outputfile.write('Case #{}: {}\n'.format(case+1, 'IMPOSSIBLE'))
    else:
        outputfile.write('Case #{}: {}\n'.format(case+1, 'POSSIBLE'))
        for r in grid:
            outputfile.write('{}\n'.format(''.join(r)))
outputfile.close()