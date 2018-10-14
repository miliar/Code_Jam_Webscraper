def solve():
    cnt = 0
    brd = []
    while cnt <= 3:
        s = raw_input().strip()
        if not len(s): continue
        brd.append(s); cnt += 1
    for i in range(4):
        cntx = sum(1 for j in range(4) if brd[i][j] == 'X')
        cnto = sum(1 for j in range(4) if brd[i][j] == 'O')
        cntt = sum(1 for j in range(4) if brd[i][j] == 'T')
        if cntx + cntt == 4: return 'X won'
        if cnto + cntt == 4: return 'O won'
    for i in range(4):
        cntx = sum(1 for j in range(4) if brd[j][i] == 'X')
        cnto = sum(1 for j in range(4) if brd[j][i] == 'O')
        cntt = sum(1 for j in range(4) if brd[j][i] == 'T')
        if cntx + cntt == 4: return 'X won'
        if cnto + cntt == 4: return 'O won'
    cntx = sum(1 for i in range(4) if brd[i][i] == 'X')
    cnto = sum(1 for i in range(4) if brd[i][i] == 'O')
    cntt = sum(1 for i in range(4) if brd[i][i] == 'T')
    if cntx + cntt == 4: return 'X won'
    if cnto + cntt == 4: return 'O won'
    cntx = sum(1 for i in range(4) if brd[i][3-i] == 'X')
    cnto = sum(1 for i in range(4) if brd[i][3-i] == 'O')
    cntt = sum(1 for i in range(4) if brd[i][3-i] == 'T')
    if cntx + cntt == 4: return 'X won'
    if cnto + cntt == 4: return 'O won'
    cnt = sum(1 for i in range(4) for j in range(4) if brd[i][j] == '.' )
    if not cnt: return 'Draw'
    else: return 'Game has not completed'

T = int(raw_input())
for i in range(1, T + 1):
    print 'Case #%d: %s' % (i, solve())