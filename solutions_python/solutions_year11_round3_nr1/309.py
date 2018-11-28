
def work(grid):
    bad = False
    while 1:
        found = False
        for row in grid:
            if '#' in row:
                found = True
                break
        if not found:
            break
        for ri, row in enumerate(grid):
            if '#' in row:
                tl = row.index('#')
                if len(row) <= tl + 1:
                    bad = True
                    break
                if row[tl + 1] != '#':
                    bad = True
                    break
                if len(grid) <= ri + 1:
                    bad = True
                    break
                if grid[ri + 1][tl] != '#' or grid[ri + 1][tl + 1] != '#':
                    bad = True
                    break
                grid[ri][tl] = '/'
                grid[ri][tl + 1] = '\\'
                grid[ri + 1][tl] = '\\'
                grid[ri + 1][tl + 1] = '/'
                break
        if bad:
            break

    if bad:
        return False
    else:
        return grid



fin = open('A-large.in')
fout = open('1ca.out', 'w')


cases = int(fin.readline())

for case_index in range(cases):
    R, C = [int(i.strip()) for i in fin.readline().split(' ')]
    grid = []
    for i in range(R):
        grid.append([c for c in fin.readline()[:C]])
    res = work(grid)
    fout.write('Case #%d:\n' % (case_index + 1))
    if not res:
        fout.write('Impossible\n')
    else:
        for r in res:
            fout.write(''.join(r) + '\n')
    print 'Case #%d' % (case_index + 1)


fin.close()
fout.close()











