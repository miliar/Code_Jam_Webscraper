with open('A-large (2).in', 'r+b') as f:
    T = int(f.readline().strip())
    for i in range(1, T+1):
        R, C = map(int, f.readline().strip().split())

        count = 0
        impossible = False
        grid = []
        for x in range(R):
            grid.append(f.readline().strip())

        for r in range(R):
            row = grid[r]
            rowstrip = row.replace('.','')
            if len(rowstrip) == 1:
                ind = row.index(rowstrip)
                colind = [x[ind] for x in grid if x[ind] != '.']
                if len(colind) == 1:
                    impossible = True
            if impossible:
                break

        if impossible:
            print "Case #%d: IMPOSSIBLE" % i
            continue

        for r in range(R):
            row = grid[r]
            rowstrip = row.replace('.','')
            if len(rowstrip) == 1 and rowstrip in '<>':
                count += 1
            elif len(rowstrip) > 1:
                if rowstrip[0] == '<':
                    count += 1
                if rowstrip[-1] == '>':
                    count += 1

        for c in range(C):
            col = ''.join([row[c] for row in grid])
            colstrip = col.replace('.','')
            if len(colstrip) == 1 and colstrip in '^v':
                count += 1
            elif len(colstrip) > 1:
                if colstrip[0] == '^':
                    count += 1
                if colstrip[-1] == 'v':
                    count += 1

        print "Case #%d: %d" % (i, count)