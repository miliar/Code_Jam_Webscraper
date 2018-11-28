#!/usr/bin/python

import sys, datetime

def solve(r, c, grid):
    global sol
    chrs = set()
    for i in xrange(r):
        for x in grid[i]:
            chrs.add(x)
    sol = None
    backtrack(grid, chrs, r, c, 0, 0)
    ret = ''
    for row in sol:
        ret += '\n' + ''.join(row)
    return ret

def backtrack(grid, chrs, r, c, i, j):
    global sol
    if sol != None:
        return
    #print i, j
    #print_grid(grid)
    if grid[i][j] != '?':
        if j == c - 1:
            if i + 1 < r:
                backtrack(grid, chrs, r, c, i + 1, 0)
            else:
                sol = [list(row) for row in grid]
        else:
            backtrack(grid, chrs, r, c, i, j + 1)
    else:
        for x in chrs:
            if sol != None:
                return
            mod = update(grid, r, c, i, j, x)
            if mod != None:
                if j == c - 1:
                    if i + 1 < r:
                        backtrack(grid, chrs, r, c, i + 1, 0)
                    else:
                        sol = [list(row) for row in grid]
                else:
                    backtrack(grid, chrs, r, c, i, j + 1)
                for (k, l) in mod:
                    grid[k][l] = '?'

def update(grid, r, c, i, j, x):
    #print_grid(grid)
    grid[i][j] = x
    i_min, i_max = (r - 1, 0)
    j_min, j_max = (c - 1, 0)
    mod = [(i, j)]
    for k in xrange(r):
        for l in xrange(c):
            if grid[k][l] == x:
                i_min = min(i_min, k)
                i_max = max(i_max, k)
                j_min = min(j_min, l)
                j_max = max(j_max, l)
    possible = True
    for k in xrange(i_min, i_max + 1):
        if not possible:
            break
        for l in xrange(j_min, j_max + 1):
            if grid[k][l] not in '?' + x:
                possible = False
            elif grid[k][l] == '?':
                grid[k][l] = x
                mod.append((k, l))
    #print x, i, j, possible
    #print i_min, i_max, j_min, j_max
    #print_grid(grid)
    #print '-----'
    if not possible:
        for (k, l) in mod:
            grid[k][l] = '?'
        return None
    return mod

def print_grid(grid):
    for r in grid:
        print ''.join(r)

def parse(input_file):
    r, c = map(int, input_file.readline().strip().split())
    grid = []
    for i in xrange(r):
        grid.append(list(input_file.readline().strip()))
    return (r, c, grid)

def main():
    start = datetime.datetime.now()
    input_file = open(sys.argv[1])
    output_file = open(sys.argv[2], "w") if len(sys.argv) > 2 else None
    print "Writing to %s" % sys.argv[2] if output_file else "No output file"
    test_cases = int(input_file.readline().strip())
    print "Test cases:",test_cases
    print '-----------------'
    for tc in xrange(1, test_cases + 1):
        output = "Case #%d: %s" % (tc, solve(*parse(input_file)))
        print output
        if output_file:
            output_file.write(output + "\n")
    print '-----------------'
    print "Written to %s" % sys.argv[2] if output_file else "No output file"
    print 'Elapsed time: %s' % (datetime.datetime.now() - start)
    input_file.close()
    if output_file:
        output_file.close()

if __name__ == "__main__":
    main()
