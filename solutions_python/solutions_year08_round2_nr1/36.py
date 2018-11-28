N = int(raw_input())

for case in range(1, N+1):
    n, A, B, C, D, x0, y0, M = map(int, raw_input().split())

    points = [(x0, y0)]
    X = x0
    Y = y0
    for i in range(1,n):
        X = (A * X + B) % M
        Y = (C * Y + D) % M
        points.append((X, Y))

    count = 0
    for i, (x0, y0) in enumerate(points):
        for j, (x1, y1) in enumerate(points[i+1:]):
            for (x2, y2) in points[i+j+2:]:
                if ((x0+x1+x2) % 3, (y0+y1+ y2) % 3) == (0,0):
                    count += 1

    print 'Case #%i: %i' %(case, count)
