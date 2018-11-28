def points(i, j, grid):
    a, b = i, j
    R, C = len(grid), len(grid[0])
    if grid[a][b] == '<':
        delta = [0, -1]
    elif grid[a][b] == '>':
        delta = [0, 1]
    elif grid[a][b] == '^':
        delta = [-1, 0]
    elif grid[a][b] == 'v':
        delta = [1, 0]
    while True:
        a += delta[0]
        b += delta[1]
        if a < 0 or a >= R or b < 0 or b >= C:
            return False
        elif grid[a][b] != '.':
            return True

def anywhere(i, j, grid):
    R, C = len(grid), len(grid[0])
    for x in ['>', '<', '^', 'v']:
        a, b = i, j
        if x == '<':
            delta = [0, -1]
        elif x == '>':
            delta = [0, 1]
        elif x == '^':
            delta = [-1, 0]
        elif x == 'v':
            delta = [1, 0]
        while True:
            a += delta[0]
            b += delta[1]
            if a < 0 or a >= R or b < 0 or b >= C:
                break
            elif grid[a][b] != '.':
                return True
    else:
        return False

g = open("data1.txt", 'w')
with open("data.txt", 'r') as f:
    T = int(f.readline())
    for r in range(T):
        R, C = [int(x) for x in f.readline().split()]
        grid = []
        for i in range(R):
            string = f.readline()
            if string[-1] == '\n':
                string = string[:-1]
            grid.append(string)

        for x in grid:
            print x

        result = 0
        impossible = 0
        for i in range(R):
            if impossible:
                break
            for j in range(C):
                if impossible:
                    break
                if grid[i][j] != '.':
                    if points(i, j, grid):
                        continue
                    elif anywhere(i, j, grid):
                        print "ANYWHERE!"
                        result += 1
                    else:
                        impossible = 1
                        break
        if impossible:
            g.write("Case #%d: IMPOSSIBLE\n" % (r+1))
        else:
            g.write("Case #%d: %d\n" % (r+1, result))

g.close()