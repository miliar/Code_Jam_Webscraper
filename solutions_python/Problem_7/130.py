import math
for case in range(input()):
    n, A, B, C, D, x0, y0, M = map(int, raw_input().split(' '))
    coords = []
    coords.append([x0, y0])
    for i in range(n - 1):
      coords.append([(A * coords[i][0] + B) % M, (C * coords[i][1] + D) % M])
    count = 0
    for i in range(len(coords)):
        for j in range(i + 1, len(coords)):
            for h in range(j + 1, len(coords)):
                cx = (coords[i][0] + coords[j][0] + coords[h][0]) / 3.0
                cy = (coords[i][1] + coords[j][1] + coords[h][1]) / 3.0
                if math.floor(cx) == cx and math.floor(cy) == cy:
                    count += 1
    print 'Case #%s: %s' % (case + 1, str(count))
