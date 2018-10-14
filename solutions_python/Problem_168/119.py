t = input()

def possible(grid, r, c):
    rs = [i for i in xrange(r) if grid[i].count('.') == c - 1]
    def col(j):
        return [ grid[i][j] for i in xrange(r) ]
    cs = [j for j in xrange(c) if col(j).count('.') == r-1]
    for r1 in rs:
        for c1 in cs:
            if grid[r1][c1] != '.':
                return False
    return True

    for i in xrange(r):
        prev = None
        good = False
        for j in xrange(c):
            if grid[i][j] != '.':
                if prev is None:
                    prev = j
                else:
                    # two in row
                    good = True
                    break
        if not good:
            return False

    for j in xrange(c):
        prev = None
        good = False
        for i in xrange(r):
            if grid[i][j] != '.':
                if prev is None:
                    prev = i
                else:
                    # two in row
                    good = True
                    break
        if not good:
            return False

    return True

def mins(grid, r, c):
    # inc j
    used = set()
    for i in xrange(r):
        for j in xrange(c):
            if grid[i][j] != '.':
                if grid[i][j] == '<':
                    used.add( (i, j) )
                break
    # dec j
    for i in xrange(r):
        for j in xrange(c-1, -1, -1):
            if grid[i][j] != '.':
                if grid[i][j] == '>':
                    used.add( (i, j) )
                break

    for j in xrange(c):
        for i in xrange(r):
            if grid[i][j] != '.':
                if grid[i][j] == '^':
                    used.add( (i, j) )
                break

    for j in xrange(c):
        for i in xrange(r-1, -1, -1):
            if grid[i][j] != '.':
                if grid[i][j] == 'v':
                    used.add( (i, j) )
                break
    return len(used)






for case in range(1, t+1):
    r, c = map(int, raw_input().split())
    grid = [raw_input() for _ in xrange(r)]
    v = None
    if not possible(grid, r, c):
        v = 'IMPOSSIBLE'
    else:
        v = str(mins(grid, r, c))
    print 'Case #%d: %s' % (case, v)
    
