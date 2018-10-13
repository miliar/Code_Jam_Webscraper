t = int(input())
for i in range(1, t+1):
    t-=1
    l = []
    state = -1
    for j in range(4):
        l.append(input())
        #l.append(list(c for c in z))
    if state == -1:
        lx = list(c.replace('T', 'X').replace('O','.') for c in l)
        lo = list(c.replace('T', 'O').replace('X','.') for c in l)
        for r in lx:#rows
            if r.count('X') == 4: state = 0
        for r in lo:
            if r.count('O') == 4: state = 1
    if state == -1:#cols
        for c in range(0, 4):
            if lx[0][c] != '.' and lx[0][c] == lx[1][c] == lx[2][c] == lx[3][c]:
                state = 0
            if lo[0][c] != '.' and lo[0][c] == lo[1][c] == lo[2][c] == lo[3][c]:
                state = 1
    if state == -1:#diags
        if (lx[0][0] != '.' and lx[0][0] == lx[1][1] == lx[2][2] == lx[3][3])\
           or (lx[3][0] != '.' and lx[3][0] == lx[2][1] == lx[1][2] == lx[0][3]):
            state = 0
        if (lo[0][0] != '.' and lo[0][0] == lo[1][1] == lo[2][2] == lo[3][3])\
           or (lo[3][0] != '.' and lo[3][0] == lo[2][1] == lo[1][2] == lo[0][3]):
            state = 1
    if state == -1:
        if sum(l.count('.') for l in l) == 0:
            state = 2
        else:
            state = 3
    print('Case #%i: %s' % (i, ['X won', 'O won', 'Draw', 'Game has not completed'][state]))
    try:
        input()
    except:
        pass
