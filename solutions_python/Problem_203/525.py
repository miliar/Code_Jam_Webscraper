with open("input.in", 'r') as f:
    with open("output.out", 'w') as g:
        T = int(f.readline())
        for r in range(T):
            R, C = [int(x) for x in f.readline().split()]
            grid = []
            for _ in range(R):
                row = f.readline().strip()
                grid.append(list(row))
            if r == 47:
                for row in grid:
                    print(row)
            order = []
            table = dict()
            for i in range(R):
                for j in range(C):
                    char = grid[i][j]
                    if char != '?':
                        if char not in table:
                            table[char] = [i, i, j, j]
                            order.append(char)
                        else:
                            table[char] = [min(i, table[char][0]), max(i, table[char][1]), min(j, table[char][2]), max(j, table[char][3])]
            if r == 30:
                print(order)
            for char in order:
                vector = table[char]
                i1, i2, j1, j2 = vector

                while True:
                    extended = False
                    # extend up
                    s = i1-1
                    if s>=0 and all([grid[s][t] == '?' for t in range(j1, j2+1)]):
                        i1 = s
                        extended = True
                    # extend down
                    s = i2 + 1
                    if s<R and all([grid[s][t] == '?' for t in range(j1, j2+1)]):
                        i2 = s
                        extended = True
                    #extend left
                    t = j1-1
                    if t>=0 and all([grid[s][t] == '?' for s in range(i1, i2 + 1)]):
                        j1 = t
                        extended = True
                    # extend right
                    t = j2 + 1
                    if t<C and all([grid[s][t] == '?' for s in range(i1, i2 + 1)]):
                        j2 = t
                        extended = True
                    # fill
                    for s in range(i1, i2+1):
                        for t in range(j1, j2+1):
                            grid[s][t] = char
                    if not extended:
                        break

            if r == 30:
                print(grid)

            g.write("Case #%d:\n" % (r + 1))
            for i in range(R):
                g.write("%s\n" % ''.join(grid[i]))

