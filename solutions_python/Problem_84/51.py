

with open("A-large.in", 'r') as f:
    with open("output.txt", 'w') as fout:
        numcases = int(f.readline())
        for i in range(1, numcases+1):
            size = f.readline().split()
            numrows = int(size[0])
            numcols = int(size[1])
            tiles = []
            for row in range(numrows):
                tiles.append([])
                line = f.readline()
                for col in range(numcols):
                    tiles[row].append(line[col])
            possible = True
            for row in range(numrows):
                for col in range(numcols):
                    if tiles[row][col] == '#':
                        if row < numrows-1 and col < numcols-1 and tiles[row+1][col] == '#' and tiles[row][col+1] == '#' and tiles[row+1][col+1] == '#':
                            tiles[row][col] = '/'
                            tiles[row+1][col] = '\\'
                            tiles[row][col+1] = '\\'
                            tiles[row+1][col+1] = '/'
                        else:
                            possible = False
                            break
            fout.write("Case #" + str(i) + ":\n")
            if not possible:
                fout.write("Impossible\n")
            else:
                for row in range(numrows):
                    for col in range(numcols):
                        fout.write(tiles[row][col])
                    fout.write('\n')
