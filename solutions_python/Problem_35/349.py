#encoding=utf-8

MAX=999999
global basin

def output(matrix, H, W):
    #Remap and print
    remap = {}
    basin = ord('a')
    for x in xrange(H):
        for y in xrange(W):
            value = remap.get(matrix[x][y])
            if value is None:
                value = basin
                remap[matrix[x][y]] = basin
                basin += 1
            print chr(value),
        print

def is_sink(map, x, y):

    minn = MAX
    for ox, oy in [(x-1,y), (x,y-1), (x,y+1), (x+1,y)]:
        try:
            minn = min(map[ox][oy], minn)
        except IndexError:
            pass #Invalid cell
    
    return map[x][y] <= minn

def dfs(x, y, result):
    global basin
    global H, W
    
    if result[x][y] is None:
        result[x][y] = basin
        basin += 1
        
    for nx, ny in [(x-1,y), (x,y-1), (x,y+1), (x+1,y)]:
        if nx < 0 or ny < 0 or nx >= H or ny >= W:
            continue
        if neighbor_visits_me(map, result, nx, ny, x, y):
            result[nx][ny] = result[x][y]
            dfs(nx, ny, result)

def neighbor_visits_me(map, result, nx, ny, x, y):
    #Verify if cell (nx, ny) visits its neighbor (x, y)
    
    if result[nx][ny] is not None:
        return False #Neighbor already has a path to go
    if map[nx][ny] <= map[x][y]:
        return False #Neighbor is lower than or equal to me

    _, mnvx, mnvy = MAX, MAX, MAX
    for nnx, nny in [(nx-1, ny), (nx, ny-1), (nx, ny+1), (nx+1, ny)]:
        if nnx >= 0 and nny >= 0:
            try:
                _, mnvx, mnvy = min((map[nnx][nny], nnx, nny), (_, mnvx, mnvy))
            except IndexError:
                pass #Invalid cell

    return x == mnvx and y == mnvy

if __name__ == '__main__':
    
    T = input()

    for case in xrange(1, T+1):
        global basin
        global H, W
        
        basin = 0
        H, W = [int(v) for v in raw_input().split()]
        
        map = []
        for _ in xrange(H):
            map.append([int(v) for v in raw_input().split()])
        
        result = [W * [None] for _ in xrange(H+2)]

        for x in xrange(H):
            for y in xrange(W):
                if is_sink(map, x, y):
                    dfs(x, y, result)
        

        print 'Case #%d:' % (case)
        output(result, H, W)