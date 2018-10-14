inp = open('1.in')

T = int(inp.readline().rstrip())
for t in range(1,T+1):
    R, C = map(int, inp.readline().rstrip().split())

    board = []

    critical = {}
    change = 0

    coltops = [-1 for i in range(C)]
    colbots = [-1 for i in range(C)]

    for rownum in range(R):
        row = inp.readline().rstrip()
        board.append(row)

        first = -1
        last  = -1
        for colnum, val in enumerate(row):
            if val != '.' and first == -1:
                # print 'WAT', first, last, rownum, colnum, val
                first = colnum
                critical[(rownum, colnum)] = critical.get((rownum, colnum), 0) + 1
                if val == '<':
                    change += 1
            if val != '.':
                last = colnum

            if val != '.' and coltops[colnum] == -1:
                coltops[colnum] = rownum
                critical[(rownum, colnum)] = critical.get((rownum, colnum), 0) + 1
                if val == '^':
                    change += 1
            if val != '.':
                colbots[colnum] = rownum

        if last != -1:
            critical[(rownum, last)] = critical.get((rownum, last), 0) + 1
            if row[last] == '>':
                change += 1

        # print critical, coltops, colbots, first, last

    for colnum in range(C):
        rownum = colbots[colnum]
        if rownum == -1:
            continue

        critical[(rownum, colnum)] = critical.get((rownum, colnum), 0) + 1
        val = board[rownum][colnum]
        if val == 'v':
            change += 1

    failed = False
    for key in critical:
        if critical[key] == 4:
            failed = True
            break

    if failed:
        change = 'IMPOSSIBLE'

    # print critical
    # print board

    print 'Case #%d: %s' % (t, change)
