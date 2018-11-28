def step(cells):
    r, c = len(cells), len(cells[0])
    result = [
        line[:] for line in cells
    ]
    for i in xrange(r):
        for j in xrange(c):
            if cells[i][j]:
                if cells[i-1][j] == 0 and cells[i][j-1] == 0:
                    result[i][j] = 0
            else:
                if cells[i-1][j] == 1 and cells[i][j-1] == 1:
                    result[i][j] = 1
    return result

def fill(cells, x1, y1, x2, y2):
    x1 -= 1
    y1 -= 1
    for c in xrange(x1, x2):
        for r in xrange(y1, y2):
            cells[r][c] = 1

def dead(cells):
    return all(cell == 0 for line in cells for cell in line)

def init(rectangles):
    maxx = max(rec[2] for rec in rectangles)
    maxy = max(rec[3] for rec in rectangles)
    result = [[0] * (maxx+1) for _ in xrange(maxy+1)]
    for rec in rectangles:
        fill(result, *rec)
    return result

def solve(rectangles):
    cells = init(rectangles)
    n = 0
    while not dead(cells):
        n += 1
        cells = step(cells)
    return n

if __name__ == '__main__':
    import sys
    rl = iter(sys.stdin).next
    for case in range(1, int(rl())+1):
        R = int(rl())
        rectangle = [map(int, rl().split()) for _ in range(R)]
        print 'Case #%d: %s' % (case, solve(rectangle))
