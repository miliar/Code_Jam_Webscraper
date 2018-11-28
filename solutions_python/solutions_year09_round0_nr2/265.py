T = int(raw_input())
INF = 20000

dydx = [(-1, 0), (0, -1), (0, 1), (1, 0)]
def search (r, c):
    global colours, letter

    if colours[r][c]:
        return colours[r][c]

    alt = terrain[r][c]
    nr, nc = None, None
    for d in dydx:
        dy, dx = d
        if terrain[r+dy][c+dx] < alt:
            alt = terrain[r+dy][c+dx]
            nr, nc = r+dy, c+dx
    if nr is not None:
        colours[r][c] = search(nr, nc)
    else:
        colours[r][c] = chr(letter)
        letter += 1
    return colours[r][c]

for cas in xrange(1, T+1):
    H, W = map(int, raw_input().split())
    terrain = [[INF]*(W+2)] + [[INF] + map(int, raw_input().split()) + [INF] for _ in xrange(H)] + [[INF]*(W+2)]
    colours = [[None]*(W+2) for _ in xrange(H+2)]
    letter = ord('a')
    print 'Case #%i:' % cas
    for r in xrange(1,H+1):
        for c in xrange(1,W+1):
            if colours[r][c] is None:
                search(r, c)
        print ' '.join(colours[r][1:-1])
