f = open('B-large.in')
T = int(f.readline().strip())
dx = [0, -1, 1, 0]
dy = [-1, 0, 0, 1]
for t in range(T):
    H, W = [int(x) for x in f.readline().strip().split()]
    map = []
    for h in range(H):
        map.append([int(x) for x in f.readline().strip().split()])
    bs = [[None]*W for h in range(H)]
    letter = 'a'
    finished = False
    while not finished:
        finished = True
        for y in range(H):
            for x in range(W):
                if bs[y][x] is None:
                    finished = False
                    break
            if not finished:
                break
        if finished:
            break
        bs[y][x] = letter
        q = [(x, y)]
        while len(q) > 0:
            x, y = q.pop()
            # Find where pos flows to
            flow = 1000000
            bx = by = -1
            for d in range(4):
                nx = x + dx[d]
                ny = y + dy[d]
                if 0<=nx<W and 0<=ny<H and map[ny][nx] < flow and map[ny][nx] < map[y][x]:
                    bx = nx
                    by = ny
                    flow = map[ny][nx]
            if bx != -1:
                assert(bs[by][bx] is None or bs[by][bx]==letter)
                if bs[by][bx] is None:
                    bs[by][bx] = letter
                    q.insert(0, (bx, by))
            # Find cells that flow in to pos
            for d in range(4):
                nx = x + dx[d]
                ny = y + dy[d]
                if 0<=nx<W and 0<=ny<H and bs[ny][nx] is None and map[ny][nx] > map[y][x]:
                    flow = 1000000
                    bx = by = -1
                    for dd in range(4):
                        mx = nx + dx[dd]
                        my = ny + dy[dd]
                        if 0<=mx<W and 0<=my<H and map[my][mx] < flow:
                            bx = mx
                            by = my
                            flow = map[my][mx]
                    if bx == x and by == y:
                        bs[ny][nx] = letter
                        q.insert(0, (nx, ny))

        letter = chr(ord(letter)+1)
    print "Case #%s:" % (t+1,)
    for h in range(H):
        for w in range(W):
            print bs[h][w],
        print
