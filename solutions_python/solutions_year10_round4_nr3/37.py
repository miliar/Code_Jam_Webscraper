EARTH = [[0 for i in range(101)]
         for j in range(101)]

def bacteria(R, rectangles):
    for rect in rectangles:
        x1, y1, x2, y2 = rect
        for x in range(x1, x2+1):
            for y in range(y1, y2+1):
                EARTH[x][y] = 1
    seconds = 0
    while True:
        ok = False
        for x in range(100, 0, -1):
            for y in range(100, 0, -1):
                if EARTH[x][y] != 0:
                    ok = True
                if EARTH[x-1][y] == 0 and EARTH[x][y-1] == 0:
                    EARTH[x][y] = 0
                if EARTH[x-1][y] == 1 and EARTH[x][y-1] == 1:
                    EARTH[x][y] = 1
        if not ok:
            break
        seconds += 1
    return seconds

if __name__ == '__main__':
    C = int(raw_input())
    for t in range(C):
        R = int(raw_input())
        rectangles = []
        for r in range(R):
            x1, y1, x2, y2 = [int(s) for s in raw_input().strip().split(' ')]
            rectangles.append((x1, y1, x2, y2))
        print 'Case #%d: %d' % (t+1, bacteria(R, rectangles))
