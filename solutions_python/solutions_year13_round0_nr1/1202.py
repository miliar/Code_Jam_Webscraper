n, = map(int, raw_input().split())

for i in range(n):
    isWin = False
    b = list()
    for j in range(4):
        b.append(list(raw_input()))
    ct = rt = None
    for r in range(4):
        for c in range(4):
            if b[r][c] == 'T':
                ct = c
                rt = r

    for t in ['X', 'O']:
        if rt != None:
            b[rt][ct] = t
        for k in range(4):
            if not isWin and b[k][0] == b[k][1] == b[k][2] == b[k][3] != '.':
                print 'Case #{}: {} won'.format(i + 1, b[k][0])
                isWin = True
                break
            if not isWin and b[0][k] == b[1][k] == b[2][k] == b[3][k] != '.':
                print 'Case #{}: {} won'.format(i + 1, b[0][k])
                isWin = True
                break
        if not isWin and b[0][0] == b[1][1] == b[2][2] == b[3][3] != '.':
            print 'Case #{}: {} won'.format(i + 1, b[0][0])
            isWin = True
            break
        if not isWin and b[0][3] == b[1][2] == b[2][1] == b[3][0] != '.':
            print 'Case #{}: {} won'.format(i + 1, b[0][3])
            isWin = True
            break
    if not isWin:
        isDraw = True
        for r in range(4):
            for c in range(4):
                if isDraw and b[r][c] == '.':
                    print 'Case #{}: Game has not completed'.format(i + 1)
                    isDraw = False
                    break
        if isDraw:
            print 'Case #{}: Draw'.format(i + 1)
    b = raw_input()
