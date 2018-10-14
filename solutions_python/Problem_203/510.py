import fileinput 

def get_letters_position(grid, r, c):
    pos = []
    for i in xrange(r):
        for j in xrange(c):
            if grid[i][j] != "?":
                pos.append([i,j])
    return pos
                
    
def fill_lines(grid, positions, r, c):
    for i, j in positions:
        cur_c = grid[i][j]
        for k in xrange(j + 1, c):
            if grid[i][k] == "?":
                grid[i][k] = cur_c
            else:
                break
        for k in xrange(j - 1, -1, -1):
            if grid[i][k] == "?":
                grid[i][k] = cur_c
            else:
                break

    for i, _ in positions:
        cur_r = grid[i]
        for k in xrange(i + 1, r):
            if grid[k][0] == "?":
                grid[k] = cur_r
            else:
                break
        for k in xrange(i - 1, -1, -1):
            if grid[k][0] == "?":
                grid[k] = cur_r
            else:
                break
    

f = fileinput.input()
sets_num = int(f.readline())
for i in xrange(sets_num):
    r, c = f.readline().strip().split(" ")
    r = int(r)
    c = int(c)

    grid = []
    for j in xrange(r):
        grid.append(list(f.readline().strip()))

    positions = get_letters_position(grid, r, c)

    fill_lines(grid, positions, r, c)
    print "Case #%d:" % (int(i) + 1 )
    for l in xrange(r):
        print "".join(grid[l])



