with open("input.txt","r") as reader, open("output.txt","w") as writer:
    cases = int(reader.readline())
    for cs in range(1,cases+1):
        rows,cols = map(int,reader.readline().split())
        grid = []
        for _ in range(rows):
            grid.append(list(reader.readline().strip()))
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] != '?':
                    filler = grid[r][c]
                    ct = c + 1
                    while ct < cols and grid[r][ct] == '?':
                        grid[r][ct] = filler
                        ct += 1
                    ct = c - 1
                    while ct >= 0 and grid[r][ct] == '?':
                        grid[r][ct] = filler
                        ct -= 1

        for r in range(rows):
            if r - 1 >= 0 and grid[r][0] == '?':
                grid[r] = grid[r-1]


        for r in reversed(range(rows)):
            if r + 1 < rows and grid[r][0] == '?':
                grid[r] = grid[r+1]

        writer.write("Case #{}:\n".format(cs))
        for r in range(rows):
            writer.write("{}\n".format(''.join(grid[r])))
                    
