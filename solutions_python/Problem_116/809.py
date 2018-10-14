f = open('A-large.in')
out = open('out', 'w')

n = int(f.readline())

def check_pts(b, points):
    x = 0
    t = 0
    o = 0
    dot_seen = False

    for p in points:
        v = b[p[0]][p[1]]
        if v == '.': dot_seen = True
        elif v == 'X': x += 1
        elif v == 'O': o += 1
        elif v == 'T': t += 1

    return (x, o, t, dot_seen)


for i in xrange(1, n+1):
    board = []
    while len(board) != 4:
        input = f.readline().strip()
        if input: board.append(input)

    dot_seen = False

    #print board
    
    # check 2 diagonals
    x, o, t, d = check_pts(board, [(0,0), (1,1), (2,2), (3,3)])
    if (x + t) == 4:
        out.write('Case #' + str(i) + ': X won\n')
        continue
    if (o + t) == 4:
        out.write('Case #' + str(i) + ': O won\n')
        continue
    if d: dot_seen = True

    x, o, t, d = check_pts(board, [(3,0), (2,1), (1,2), (0,3)])
    if (x + t) == 4:
        out.write('Case #' + str(i) + ': X won\n')
        continue
    if (o + t) == 4:
        out.write('Case #' + str(i) + ': O won\n')
        continue
    if d: dot_seen = True

    # check normal lines
    #br = False
    for j in xrange(4):
        x, o, t, d = check_pts(board, [(j,0), (j,1), (j,2), (j,3)])
        if (x + t) == 4:
            out.write('Case #' + str(i) + ': X won\n')
            break
        if (o + t) == 4:
            out.write('Case #' + str(i) + ': O won\n')
            break
        if d: dot_seen = True

        x, o, t, d = check_pts(board, [(0,j), (1,j), (2,j), (3,j)])
        if (x + t) == 4:
            out.write('Case #' + str(i) + ': X won\n')
            break
        if (o + t) == 4:
            out.write('Case #' + str(i) + ': O won\n')
            break
        if d: dot_seen = True
    else:
        if dot_seen: out.write('Case #' + str(i) + ': Game has not completed\n')
        else: out.write('Case #' + str(i) + ': Draw\n')

