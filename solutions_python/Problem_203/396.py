
def rrange(a, b):
    i = min(a[0], b[0])
    j = max(a[0], b[0])
    return range(i, j + 1)


def crange(a, b):
    i = min(a[1], b[1])
    j = max(a[1], b[1])
    return range(i, j + 1)

def singlehit(grid, a, b):
    found = ''
    for x in rrange(a, b):
        for y in crange(a, b):
            if grid[x][y] != '?':
                if found == '':
                    found = grid[x][y]
                if grid[x][y] == found:
                    continue
                else:
                    return False
    return True

def trygrow(a, b, grid):
    i,j,k,l = a[0],a[1],b[0],b[1]
    if j > 0 and singlehit(grid,(i,j-1),b):
        return True, (i,j-1),b
    if l < len(grid[0])-1 and singlehit(grid,a,(k, l+1)):
        return True, a,(k, l+1)
    if i > 0 and singlehit(grid, (i-1,j),b):
        return True, (i-1,j),b
    if k < len(grid)-1 and singlehit(grid,a,(k+1, l)):
        return True, a,(k+1, l)
    return False, a,b

def solve(representation):
    R, C, grid = representation
    # print(pancakes, spatula)
    print(R, C)
    [print(r) for r in grid]

    locs = []
    for i in range(R):
        for j in range(C):
            if grid[i][j] != '?':
                locs.append((i,j))

    for loc in locs:
        # just grow these as big as possible.
        workdone = True
        a,b=loc, loc
        while workdone:
            workdone, a, b = trygrow(a,b, grid)
        for i in rrange(a,b):
            for j in crange(a,b):
                grid[i][j] = grid[loc[0]][loc[1]]




    return '\n' + '\n'.join([''.join(line) for line in grid])



def getprob(content):
    R, C = (int(l) for l in content[0].split(' '))
    grid = [[char for char in line] for line in content[1:1 + R]]
    del content[:1 + R]
    return R, C, grid


def parseprob(prob):
    return prob


def readAndSolve():
    d = "C:\\Users\\dave\\Downloads\\"
    infile = "A-large.in"
    content = []
    with open(d + infile) as f:
        content = f.readlines()
    content = [x.strip() for x in content]
    numprobs = int(content[0])
    del content[0]

    lines = []
    for pnum in range(numprobs):
        prob = getprob(content)
        representation = parseprob(prob)
        solved = solve(representation)
        str = 'Case #{}: {}'.format(pnum + 1, solved)
        print(str)
        lines.append(str)

    outfname = infile.replace(".in", ".out")
    outfile = "C:\\Users\\dave\\PycharmProjects\\codejam_2017_1a\\" + outfname
    f = open(outfile, 'w')
    print('\n'.join(lines), file=f)
    f.close()


readAndSolve()
