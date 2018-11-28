problem  = 'C'
attemptN = 2
size     = 'small'

if size == 'small':
    filename = '%s-%s-attempt%d' % (problem, size, attemptN)
else:
    filename = '%s-%s' % (problem, size)


# todo: unroll loop
def wouldAdd(grid, r, c):
    rMin = max(0, r-1)
    rMax = min(len(grid), r+2)
    cMin = max(0, c-1)
    cMax = min(len(grid[0]), c+2)
    wA = 0
    for r in range(rMin, rMax):
        for c in range(cMin, cMax):
            wA += grid[r][c] == '*'
    return wA

# todo: unroll loop
def add(grid, r, c):
    rMin = max(0, r-1)
    rMax = min(len(grid), r+2)
    cMin = max(0, c-1)
    cMax = min(len(grid[0]), c+2)
    wA = 0
    for r in range(rMin, rMax):
        for c in range(cMin, cMax):
            grid[r][c] = '.'
    return grid

def placeFree(grid, freeSpaces):
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if grid[r][c] != '.':
                continue
            
            wA = wouldAdd(grid, r, c)
            if wA > 0 and wA <= freeSpaces:
                grid = add(grid, r, c)
                return (grid, wA)
    return (grid, 0)
                
            

with open(filename+'.in', 'r') as f, open(filename+'.out', 'w') as out:
    samples = int(f.readline())
    for testN in range(samples):
        R, C, M = [int(x) for x in f.readline().split()]
        freeSpaces = R*C - M

        if freeSpaces < 1:
            output = 'Impossible'
        else:
            for r in range(R):
                for c in range(C):
                    freeSpaces = R*C - M
                    
                    grid = [['*' for _ in range(C)] for _ in range(R)]
                    grid[r][c] = '.'
                    freeSpaces -= 1
                    while freeSpaces > 0:
                        grid, wA = placeFree(grid, freeSpaces)
                        if wA <= 0:
                            output = 'Impossible'
                            break

                        freeSpaces -= wA
                    grid[r][c] = 'c'

                    if freeSpaces == 0:
                        output = '\n'.join([''.join(grid[i]) for i in range(len(grid))])
                        break
                if freeSpaces == 0:
                    break
            
            if freeSpaces != 0:
                output = 'Impossible'
            
        
        out.write("Case #%d:\n%s\n" % (testN+1, output))
