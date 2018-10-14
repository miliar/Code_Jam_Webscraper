def center_is_integer((x1, y1), (x2, y2) , (x3, y3)):
    x = float(x1 + x2 + x3) / 3
    y = float(y1 + y2 + y3) / 3
    if (x % 1 == 0) and (y % 1 == 0):
        return True
    else:
        return False

for case in range(input()):
    n, A, B, C, D, x0, y0, M = map(int,raw_input().split())
    X = x0
    Y = y0
    coordinates = []
    coordinates.append((X,Y))
    for i in range(n-1):
        X = (A * X + B) % M 
        Y = (C * Y + D) % M
        coordinates.append((X,Y))
    output = 0
    for row1 in range(n-2):
        for row2 in range(row1+1, n):
            for row3 in range(row2+1, n):
                if center_is_integer(coordinates[row1], coordinates[row2], coordinates[row3]):
                    output += 1
    
    print "Case #%d: %d" % (case + 1, output)